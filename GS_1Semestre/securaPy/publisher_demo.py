"""
Demo: roda o servidor de alertas em background e permite disparar
alertas manualmente pelo terminal para testar broadcast a multiplos clientes.

Uso:
    1. Terminal 1: python publisher_demo.py
    2. Terminal 2 (e 3, 4...): python cliente_alertas.py
    3. No terminal 1, pressione ENTER para disparar um alerta de exemplo.
"""

import threading
import time

from servidor_alertas import iniciar_servidor, broadcast_alerta


_ALERTAS_DEMO = [
    {
        "timestamp": "2025-02-20 08:15:01",
        "regra_id": "R001",
        "regra_nome": "Login com Usuario Privilegiado",
        "severidade": "MEDIA",
        "ip": "185.220.101.1",
        "descricao": "Tentativa de login com usuario admin",
    },
    {
        "timestamp": "2025-02-20 08:10:02",
        "regra_id": "R002",
        "regra_nome": "Acesso a Porta Critica Bloqueado",
        "severidade": "ALTA",
        "ip": "91.240.118.172",
        "descricao": "Acesso bloqueado a porta critica 22",
    },
    {
        "timestamp": "2025-02-20 08:20:08",
        "regra_id": "R003",
        "regra_nome": "Tentativa de Path Traversal",
        "severidade": "CRITICA",
        "ip": "91.240.118.172",
        "descricao": "Path traversal detectado na URL /../../etc/passwd",
    },
]


def main():
    thread = threading.Thread(target=iniciar_servidor, daemon=True)
    thread.start()
    time.sleep(0.5)

    print("\n[DEMO] Servidor rodando em background.")
    print("[DEMO] Conecte clientes em outros terminais: python cliente_alertas.py")
    print("[DEMO] Pressione ENTER para disparar o proximo alerta (Ctrl+C para sair).\n")

    indice = 0
    try:
        while True:
            input(f"-> ENTER para enviar alerta #{indice + 1}... ")
            alerta = _ALERTAS_DEMO[indice % len(_ALERTAS_DEMO)]
            broadcast_alerta(alerta)
            print(f"[DEMO] Enviado: {alerta['regra_nome']} ({alerta['ip']})\n")
            indice += 1
    except KeyboardInterrupt:
        print("\n[DEMO] Encerrando.")


if __name__ == "__main__":
    main()
