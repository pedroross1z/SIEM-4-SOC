"""
SecuraPy SIEM - Ponto de Entrada Principal
Integra todos os modulos: coletor, regras, detector, enriquecimento,
servidor de alertas e relatorios em um menu interativo.
"""

import os
from datetime import datetime

from coletor import carregar_todos_os_logs
from regras import carregar_regras, aplicar_regras
from detector import (
    detectar_brute_force,
    detectar_brute_force_temporal,
    detectar_port_scan,
    verificar_blacklist,
    gerar_resumo_ameacas,
)
from enriquecimento import enriquecer_alertas, exibir_enriquecimento
from relatorios import (
    exibir_menu,
    resumo_geral,
    filtrar_eventos,
    buscar_ip,
    top_ips,
    exportar_relatorio_json,
    exibir_tabela,
    criar_regra_interativa,
)
from integridade import salvar_hashes, verificar_hashes
from gerador_logs import gerar_logs

# Configuracoes
PASTA_BASE = os.path.dirname(os.path.abspath(__file__))
PASTA_LOGS = os.path.join(PASTA_BASE, "logs")
ARQUIVO_REGRAS = os.path.join(PASTA_BASE, "config", "regras.json")
ARQUIVO_HASHES = os.path.join(PASTA_BASE, "config", "hashes.json")
PASTA_SAIDA = os.path.join(PASTA_BASE, "saida")
BLACKLIST = {"185.220.101.1", "45.33.32.156", "91.240.118.172", "23.94.5.100"}


def _exige_dados(eventos):
    if not eventos:
        print("\n[AVISO] Carregue os logs primeiro (opcao 1).")
        return False
    return True


def _input_opcional(label):
    valor = input(f"{label} (ENTER para ignorar): ").strip()
    return valor or None


def _carregar_e_processar():
    eventos = carregar_todos_os_logs(PASTA_LOGS)
    regras = carregar_regras(ARQUIVO_REGRAS)
    alertas = aplicar_regras(eventos, regras)

    brute = detectar_brute_force(eventos)
    scan = detectar_port_scan(eventos)
    bl = verificar_blacklist(eventos, BLACKLIST)
    resumo = gerar_resumo_ameacas(brute, scan, bl)

    print(f"\n[OK] {len(eventos)} eventos carregados.")
    print(f"[OK] {len(regras)} regras ativas, {len(alertas)} alertas gerados.")
    print(f"[OK] {len(resumo)} ameacas consolidadas.")
    return eventos, alertas, resumo, brute, scan, bl


def _alertas_por_severidade(alertas):
    sev = input("Severidade (CRITICA/ALTA/MEDIA/BAIXA/INFO): ").strip().upper()
    if not sev:
        print("[AVISO] Severidade vazia.")
        return
    filtrados = [a for a in alertas if a.get("severidade") == sev]
    if not filtrados:
        print(f"Nenhum alerta com severidade {sev}.")
        return
    exibir_tabela(filtrados, ["timestamp", "regra_id", "regra_nome", "ip", "descricao"])


def _exportar(eventos, alertas, resumo):
    nome = f"relatorio_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
    caminho = os.path.join(PASTA_SAIDA, nome)
    dados = {
        "gerado_em": datetime.now().isoformat(timespec="seconds"),
        "total_eventos": len(eventos),
        "total_alertas": len(alertas),
        "fontes": {
            "auth": len(filtrar_eventos(eventos, fonte="auth")),
            "firewall": len(filtrar_eventos(eventos, fonte="firewall")),
            "web": len(filtrar_eventos(eventos, fonte="web")),
        },
        "top_ips": top_ips(eventos, n=10),
        "alertas": alertas,
        "ameacas": resumo,
    }
    exportar_relatorio_json(dados, caminho)


_SUBMENU_BONUS = """
+------------------------------------------+
|       Funcionalidades Bonus              |
+------------------------------------------+
|  A. Correlacao temporal (brute force)    |
|  B. Hash de integridade dos logs         |
|  C. Gerar logs sinteticos                |
|  D. Criar nova regra customizada         |
|  V. Voltar                               |
+------------------------------------------+
"""


def _submenu_bonus(eventos):
    print(_SUBMENU_BONUS)
    escolha = input("Escolha (A/B/C/D/V): ").strip().upper()

    if escolha == "A":
        if not _exige_dados(eventos):
            return
        try:
            janela = int(input("Janela em segundos (padrao 60): ").strip() or "60")
            thr = int(input("Threshold de tentativas (padrao 5): ").strip() or "5")
        except ValueError:
            print("[ERRO] Valor invalido.")
            return
        resultado = detectar_brute_force_temporal(eventos, threshold=thr, janela_segundos=janela)
        if not resultado:
            print(f"Nenhum brute force detectado em janelas de {janela}s.")
            return
        for ip, dados in resultado.items():
            print(f"\n[{dados['severidade']}] {ip}")
            print(f"  Pico: {dados['tentativas_pico']} tentativas em {dados['duracao_segundos']}s")
            print(f"  Janela: {dados['janela_inicio']} -> {dados['janela_fim']}")
            print(f"  Usuarios: {dados['usuarios']}")

    elif escolha == "B":
        print("\n1. Salvar hashes atuais")
        print("2. Verificar integridade")
        sub = input("Opcao: ").strip()
        if sub == "1":
            salvar_hashes(PASTA_LOGS, ARQUIVO_HASHES)
        elif sub == "2":
            relatorio = verificar_hashes(PASTA_LOGS, ARQUIVO_HASHES)
            if not relatorio:
                return
            for nome, status in relatorio.items():
                marcador = "[OK]" if status == "OK" else f"[{status}]"
                print(f"  {marcador:<14} {nome}")
        else:
            print("[ERRO] Opcao invalida.")

    elif escolha == "C":
        pasta = input("Pasta de saida (padrao logs_gerados): ").strip() or "logs_gerados"
        try:
            n = int(input("Linhas por arquivo (padrao 50): ").strip() or "50")
            prop = float(input("Proporcao de ataques 0.0-1.0 (padrao 0.3): ").strip() or "0.3")
        except ValueError:
            print("[ERRO] Valor invalido.")
            return
        gerar_logs(os.path.join(PASTA_BASE, pasta) if not os.path.isabs(pasta) else pasta, n, prop)

    elif escolha == "D":
        criar_regra_interativa(ARQUIVO_REGRAS)

    elif escolha == "V":
        return

    else:
        print(f"[ERRO] Opcao desconhecida: {escolha}")


def main():
    eventos = []
    alertas = []
    resumo = []
    cache_enriquecimento = {}

    print("=" * 50)
    print("       SecuraPy SIEM - Coding for Security")
    print("=" * 50)

    while True:
        opcao = exibir_menu()

        if opcao == -1:
            print("[ERRO] Opcao invalida. Tente novamente.")
            continue

        if opcao == 1:
            eventos, alertas, resumo, _, _, _ = _carregar_e_processar()

        elif opcao == 2:
            if not _exige_dados(eventos):
                continue
            resumo_geral(eventos, alertas)

        elif opcao == 3:
            if not _exige_dados(eventos):
                continue
            fonte = _input_opcional("Fonte (auth/firewall/web)")
            tipo = _input_opcional("Tipo (FAIL/BLOCK/GET/...)")
            ip = _input_opcional("IP")
            resultado = filtrar_eventos(eventos, fonte=fonte, tipo=tipo, ip=ip)
            print(f"\n{len(resultado)} eventos correspondem.")
            exibir_tabela(resultado, ["timestamp", "fonte", "tipo", "ip", "detalhes"])

        elif opcao == 4:
            if not _exige_dados(eventos):
                continue
            ip = input("IP a buscar: ").strip()
            if ip:
                buscar_ip(ip, eventos, alertas, cache_enriquecimento)

        elif opcao == 5:
            if not _exige_dados(eventos):
                continue
            ranking = top_ips(eventos, n=10)
            exibir_tabela(
                [{"ip": ip, "eventos": qtd} for ip, qtd in ranking],
                ["ip", "eventos"],
            )

        elif opcao == 6:
            if not _exige_dados(eventos):
                continue
            _alertas_por_severidade(alertas)

        elif opcao == 7:
            if not _exige_dados(eventos):
                continue
            alertas = enriquecer_alertas(alertas, cache_enriquecimento)
            print(f"[OK] {len(cache_enriquecimento)} IPs no cache de enriquecimento.")
            for ip, geo in list(cache_enriquecimento.items())[:5]:
                print()
                exibir_enriquecimento(geo)

        elif opcao == 8:
            if not _exige_dados(eventos):
                continue
            _exportar(eventos, alertas, resumo)

        elif opcao == 9:
            from servidor_alertas import iniciar_servidor
            print("[INFO] Iniciando servidor de alertas (Ctrl+C para encerrar)...")
            iniciar_servidor()

        elif opcao == 10:
            _submenu_bonus(eventos)

        elif opcao == 0:
            print("Encerrando SecuraPy. Ate logo!")
            break


if __name__ == "__main__":
    main()
