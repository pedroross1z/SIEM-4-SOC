"""
Modulo Bonus - Gerador de Logs Sinteticos
Cria arquivos auth.log, firewall.log e web_access.log com mistura de
trafego normal e cenarios de ataque (brute force, port scan, XSS, traversal).

Uso:
    python gerador_logs.py [pasta_saida] [--linhas N] [--ataques 0.3]
"""

import argparse
import os
import random
from datetime import datetime, timedelta


_IPS_INTERNOS = ["192.168.1.10", "192.168.1.20", "192.168.1.45", "10.0.0.5"]
_IPS_EXTERNOS_BENIGNOS = ["8.8.8.8", "1.1.1.1", "201.10.20.30", "189.45.67.89"]
_IPS_ATACANTES = ["185.220.101.1", "91.240.118.172", "45.33.32.156", "23.94.5.100"]

_USUARIOS_NORMAIS = ["carlos", "ana", "bruno", "diana", "eduardo", "fernanda"]
_USUARIOS_PRIVILEGIADOS = ["admin", "root", "sa", "oracle", "administrator"]

_PORTAS_CRITICAS = [22, 23, 3389, 445, 3306, 5432, 1433]
_PORTAS_NORMAIS = [80, 443, 8080, 53]

_URLS_NORMAIS = ["/index.html", "/sobre", "/contato", "/produtos", "/api/v1/users", "/static/css/main.css"]
_URLS_RECON = ["/wp-admin", "/phpmyadmin", "/shell.php", "/.env", "/admin", "/wp-login.php"]
_URLS_TRAVERSAL = ["/../../etc/passwd", "/../etc/shadow", "/../../../etc/passwd"]
_URLS_XSS = ["/search?q=<script>alert(1)</script>", "/comment?text=<script>", "/page?onerror=alert(1)"]


def _ts(base, offset_segundos):
    return (base + timedelta(seconds=offset_segundos)).strftime("%Y-%m-%d %H:%M:%S")


def gerar_auth(n_linhas, prop_ataques, base):
    """Gera linhas de auth.log misturando OK/FAIL benigno e brute force."""
    linhas = []
    for i in range(n_linhas):
        ts = _ts(base, i * random.randint(1, 4))
        if random.random() < prop_ataques:
            ip = random.choice(_IPS_ATACANTES)
            usuario = random.choice(_USUARIOS_PRIVILEGIADOS)
            linhas.append(f"{ts} FAIL usuario={usuario} ip={ip}")
        else:
            ip = random.choice(_IPS_INTERNOS)
            usuario = random.choice(_USUARIOS_NORMAIS)
            tipo = "OK" if random.random() > 0.1 else "FAIL"
            linhas.append(f"{ts} {tipo} usuario={usuario} ip={ip}")
    return linhas


def gerar_firewall(n_linhas, prop_ataques, base):
    """Gera linhas de firewall.log misturando ALLOW benigno e BLOCK em portas criticas."""
    linhas = []
    for i in range(n_linhas):
        ts = _ts(base, i * random.randint(1, 5))
        if random.random() < prop_ataques:
            ip = random.choice(_IPS_ATACANTES)
            porta = random.choice(_PORTAS_CRITICAS)
            linhas.append(f"{ts} BLOCK proto=TCP src={ip} dst=10.0.0.1 dport={porta}")
        else:
            ip = random.choice(_IPS_INTERNOS + _IPS_EXTERNOS_BENIGNOS)
            porta = random.choice(_PORTAS_NORMAIS)
            linhas.append(f"{ts} ALLOW proto=TCP src={ip} dst=10.0.0.1 dport={porta}")
    return linhas


def gerar_web(n_linhas, prop_ataques, base):
    """Gera linhas de web_access.log misturando GETs normais com recon/XSS/traversal."""
    linhas = []
    for i in range(n_linhas):
        ts = _ts(base, i * random.randint(1, 6))
        if random.random() < prop_ataques:
            ip = random.choice(_IPS_ATACANTES)
            categoria = random.choice([_URLS_RECON, _URLS_TRAVERSAL, _URLS_XSS])
            url = random.choice(categoria)
            status = random.choice([400, 403, 404])
            linhas.append(f"{ts} GET url={url} ip={ip} status={status}")
        else:
            ip = random.choice(_IPS_INTERNOS + _IPS_EXTERNOS_BENIGNOS)
            url = random.choice(_URLS_NORMAIS)
            linhas.append(f"{ts} GET url={url} ip={ip} status=200")
    return linhas


def gerar_logs(pasta_saida, linhas_por_arquivo=50, prop_ataques=0.3):
    """Gera os 3 arquivos de log na pasta indicada."""
    os.makedirs(pasta_saida, exist_ok=True)
    base = datetime.now() - timedelta(hours=1)

    arquivos = {
        "auth.log": gerar_auth(linhas_por_arquivo, prop_ataques, base),
        "firewall.log": gerar_firewall(linhas_por_arquivo, prop_ataques, base),
        "web_access.log": gerar_web(linhas_por_arquivo, prop_ataques, base),
    }

    for nome, linhas in arquivos.items():
        caminho = os.path.join(pasta_saida, nome)
        with open(caminho, "w", encoding="utf-8") as f:
            f.write("\n".join(linhas) + "\n")
        print(f"[OK] {len(linhas)} linhas em {caminho}")


def _cli():
    parser = argparse.ArgumentParser(description="Gera logs sinteticos para o SecuraPy.")
    parser.add_argument("pasta", nargs="?", default="logs_gerados",
                        help="Pasta de saida (padrao: logs_gerados)")
    parser.add_argument("--linhas", type=int, default=50,
                        help="Linhas por arquivo (padrao: 50)")
    parser.add_argument("--ataques", type=float, default=0.3,
                        help="Proporcao de eventos de ataque (0.0-1.0, padrao: 0.3)")
    parser.add_argument("--seed", type=int, default=None,
                        help="Semente do random para resultados reproduziveis")
    args = parser.parse_args()

    if args.seed is not None:
        random.seed(args.seed)

    gerar_logs(args.pasta, args.linhas, args.ataques)


if __name__ == "__main__":
    _cli()
