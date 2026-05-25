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
)

# Configuracoes
PASTA_BASE = os.path.dirname(os.path.abspath(__file__))
PASTA_LOGS = os.path.join(PASTA_BASE, "logs")
ARQUIVO_REGRAS = os.path.join(PASTA_BASE, "config", "regras.json")
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

        elif opcao == 0:
            print("Encerrando SecuraPy. Ate logo!")
            break


if __name__ == "__main__":
    main()
