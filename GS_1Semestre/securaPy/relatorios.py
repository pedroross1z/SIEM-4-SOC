"""
Modulo 6 - Dashboard CLI e Relatorios
Interface interativa do SIEM com menu de opcoes, filtros de eventos,
busca por IP, ranking de ameacas e exportacao de relatorios em JSON.
"""

import json
import os


_MENU = """
+==========================================+
|         SecuraPy SIEM - Menu             |
+==========================================+
|  1. Carregar e processar logs            |
|  2. Resumo geral                         |
|  3. Filtrar eventos                      |
|  4. Buscar IP                            |
|  5. Top 10 IPs suspeitos                 |
|  6. Ver alertas por severidade           |
|  7. Enriquecer IPs suspeitos             |
|  8. Exportar relatorio JSON              |
|  9. Iniciar servidor de alertas          |
| 10. Funcionalidades bonus                |
|  0. Sair                                 |
+==========================================+
"""


def exibir_menu():
    """Exibe o menu principal e retorna a opcao (int) ou -1 se invalido."""
    print(_MENU)
    try:
        opcao = int(input("Escolha uma opcao: ").strip())
    except (ValueError, EOFError):
        return -1
    if opcao < 0 or opcao > 10:
        return -1
    return opcao


def resumo_geral(eventos, alertas):
    """Imprime contadores de eventos por fonte e alertas por severidade."""
    print("\n=== RESUMO GERAL ===")
    print(f"Total de eventos: {len(eventos)}")
    print(f"Total de alertas: {len(alertas)}")

    por_fonte = {}
    for ev in eventos:
        fonte = ev.get("fonte", "?")
        por_fonte[fonte] = por_fonte.get(fonte, 0) + 1

    if por_fonte:
        print("\nEventos por fonte:")
        for fonte, qtd in sorted(por_fonte.items()):
            print(f"  {fonte:<10} {qtd}")

    por_sev = {}
    for a in alertas:
        sev = a.get("severidade", "?")
        por_sev[sev] = por_sev.get(sev, 0) + 1

    if por_sev:
        ordem = ["CRITICA", "ALTA", "MEDIA", "BAIXA", "INFO"]
        print("\nAlertas por severidade:")
        for sev in ordem:
            if sev in por_sev:
                print(f"  {sev:<10} {por_sev[sev]}")
        for sev, qtd in por_sev.items():
            if sev not in ordem:
                print(f"  {sev:<10} {qtd}")


def filtrar_eventos(eventos, fonte=None, tipo=None, ip=None):
    """Filtra eventos por fonte, tipo e/ou ip. Criterios None sao ignorados."""
    return [
        e for e in eventos
        if (fonte is None or e.get("fonte") == fonte)
        and (tipo is None or e.get("tipo") == tipo)
        and (ip is None or e.get("ip") == ip)
    ]


def buscar_ip(ip, eventos, alertas, cache_enriquecimento):
    """Exibe relatorio completo de um IP: eventos, alertas e geolocalizacao."""
    print(f"\n=== BUSCA POR IP: {ip} ===")

    eventos_ip = filtrar_eventos(eventos, ip=ip)
    alertas_ip = [a for a in alertas if a.get("ip") == ip]

    print(f"Eventos relacionados: {len(eventos_ip)}")
    print(f"Alertas gerados:      {len(alertas_ip)}")

    if eventos_ip:
        por_fonte = {}
        for ev in eventos_ip:
            f = ev.get("fonte", "?")
            por_fonte[f] = por_fonte.get(f, 0) + 1
        print("\nDistribuicao por fonte:")
        for f, qtd in sorted(por_fonte.items()):
            print(f"  {f:<10} {qtd}")

    if alertas_ip:
        print("\nAlertas:")
        for a in alertas_ip:
            print(f"  [{a.get('severidade','?')}] {a.get('regra_nome','?')} - {a.get('descricao','')}")

    geo = cache_enriquecimento.get(ip)
    if geo:
        print("\nGeolocalizacao (cache):")
        print(f"  Cidade:  {geo.get('cidade','-')}")
        print(f"  Regiao:  {geo.get('regiao','-')}")
        print(f"  Pais:    {geo.get('pais','-')}")
        print(f"  Org:     {geo.get('org','-')}")
    else:
        print("\nGeolocalizacao: nao consultada (rode opcao 7 antes).")


def top_ips(eventos, n=10):
    """Retorna lista de tuplas (ip, contagem) ordenada decrescente, limitada a N."""
    contagem = {}
    for ev in eventos:
        ip = ev.get("ip")
        if not ip:
            continue
        contagem[ip] = contagem.get(ip, 0) + 1

    ranking = sorted(contagem.items(), key=lambda x: x[1], reverse=True)
    return ranking[:n]


def _serializar(obj):
    """Converte sets em listas recursivamente para JSON."""
    if isinstance(obj, set):
        return sorted(obj, key=str)
    if isinstance(obj, dict):
        return {k: _serializar(v) for k, v in obj.items()}
    if isinstance(obj, (list, tuple)):
        return [_serializar(v) for v in obj]
    return obj


def exportar_relatorio_json(dados, caminho):
    """Salva um relatorio completo em formato JSON (indent=2, ensure_ascii=False)."""
    pasta = os.path.dirname(caminho)
    if pasta:
        os.makedirs(pasta, exist_ok=True)

    try:
        with open(caminho, "w", encoding="utf-8") as f:
            json.dump(_serializar(dados), f, indent=2, ensure_ascii=False)
        print(f"[OK] Relatorio salvo em: {caminho}")
    except OSError as e:
        print(f"[ERRO] Nao foi possivel salvar {caminho}: {e}")


_CONDICOES_VALIDAS = {
    "usuario_privilegiado": ("auth", "usuarios_alvo", "Lista de usuarios alvo (separados por virgula)"),
    "porta_critica":        ("firewall", "portas_criticas", "Lista de portas criticas (numeros separados por virgula)"),
    "path_traversal":       ("web", "padroes", "Lista de padroes de path traversal (separados por virgula)"),
    "xss":                  ("web", "padroes", "Lista de padroes de XSS (separados por virgula)"),
    "reconhecimento":       ("web", "urls_suspeitas", "Lista de URLs suspeitas (separadas por virgula)"),
}


def criar_regra_interativa(caminho_regras):
    """Cria nova regra via prompt e adiciona ao arquivo regras.json existente."""
    print("\n=== CRIAR NOVA REGRA ===")
    print(f"Condicoes disponiveis: {', '.join(_CONDICOES_VALIDAS)}")

    condicao = input("Condicao: ").strip()
    if condicao not in _CONDICOES_VALIDAS:
        print(f"[ERRO] Condicao invalida: {condicao}")
        return False

    fonte_esperada, campo_lista, prompt_lista = _CONDICOES_VALIDAS[condicao]

    id_regra = input("ID (ex: R006): ").strip().upper()
    nome = input("Nome: ").strip()
    descricao = input("Descricao: ").strip()
    print(f"Fonte sera fixada como: {fonte_esperada}")

    valores_raw = input(f"{prompt_lista}: ").strip()
    valores = [v.strip() for v in valores_raw.split(",") if v.strip()]
    if not valores:
        print("[ERRO] Lista vazia.")
        return False

    if campo_lista == "portas_criticas":
        try:
            valores = [int(v) for v in valores]
        except ValueError:
            print("[ERRO] Portas devem ser numeros inteiros.")
            return False

    try:
        severidade_base = int(input("Severidade base (0-10): ").strip())
    except ValueError:
        print("[ERRO] Severidade deve ser inteiro.")
        return False

    if not id_regra or not nome:
        print("[ERRO] ID e nome sao obrigatorios.")
        return False

    nova = {
        "id": id_regra,
        "nome": nome,
        "descricao": descricao,
        "fonte": fonte_esperada,
        "condicao": condicao,
        campo_lista: valores,
        "severidade_base": severidade_base,
        "ativa": True,
    }

    try:
        with open(caminho_regras, "r", encoding="utf-8") as f:
            dados = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        dados = {"regras": []}

    regras = dados.get("regras", [])
    if any(r.get("id") == id_regra for r in regras):
        print(f"[ERRO] Ja existe regra com id {id_regra}.")
        return False

    regras.append(nova)
    dados["regras"] = regras

    pasta = os.path.dirname(caminho_regras)
    if pasta:
        os.makedirs(pasta, exist_ok=True)
    with open(caminho_regras, "w", encoding="utf-8") as f:
        json.dump(dados, f, indent=2, ensure_ascii=False)

    print(f"[OK] Regra {id_regra} adicionada em {caminho_regras}")
    return True


def exibir_tabela(dados, colunas):
    """Exibe uma lista de dicionarios como tabela formatada no terminal."""
    if not dados:
        print("Nenhum dado encontrado.")
        return

    larguras = {}
    for col in colunas:
        max_dado = max((len(str(d.get(col, ""))) for d in dados), default=0)
        larguras[col] = max(len(col), max_dado)

    cabecalho = "  ".join(f"{col:<{larguras[col]}}" for col in colunas)
    separador = "  ".join("-" * larguras[col] for col in colunas)
    print(cabecalho)
    print(separador)

    for d in dados:
        linha = "  ".join(f"{str(d.get(col, '')):<{larguras[col]}}" for col in colunas)
        print(linha)
