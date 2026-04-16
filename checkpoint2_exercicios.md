# Check Point 02 — Coding for Security

## Conteúdo avaliado: Aulas 6, 7 e 8
- **Aula 6:** Estruturas de repetição (for, while, range, break, continue)
- **Aula 7:** Listas, tuplas, dicionários e sets
- **Aula 8:** Tratamento de exceções (try/except/else/finally, raise)

**Cada exercício vale 1 ponto. Nota máxima: 10.**

---

> **Exercício 1 — Contador de Vogais e Consoantes:** Crie um programa que peça uma frase ao usuário e use um laço `for` para percorrer cada caractere, contando quantas vogais e quantas consoantes existem. Ignore números, espaços e caracteres especiais. Exiba o total de cada um ao final.
>
> ```python
> # Teste com estas frases:
> testes = [
>     "Python para Seguranca",
>     "Hello World 123!",
>     "aeiou",
>     "",
> ]
>
> # Saída esperada (frase 1):
> # Frase: "Python para Seguranca"
> # Vogais: 7
> # Consoantes: 11
> ```

---

> **Exercício 2 — Validador de Senha com Regras:** Crie um programa que peça uma senha ao usuário repetidamente (usando `while`) até que ela atenda TODOS os critérios: mínimo 8 caracteres, pelo menos 1 letra maiúscula, pelo menos 1 letra minúscula, pelo menos 1 número e pelo menos 1 caractere especial (`!@#$%&*`). A cada tentativa inválida, informe quais critérios não foram atendidos. Use `break` para sair quando a senha for válida.
>
> ```python
> # Teste com estas senhas:
> testes = [
>     "abc",              # Fraca: faltam maiúscula, número, especial, < 8 chars
>     "abcdefgh",         # Faltam maiúscula, número, especial
>     "Abcdefgh",         # Faltam número e especial
>     "Abcdefg1",         # Falta especial
>     "Cyber@2024",       # Válida!
> ]
>
> # Saída esperada (senha "Abcdefgh"):
> # Senha inválida! Problemas encontrados:
> # - Falta pelo menos 1 número
> # - Falta pelo menos 1 caractere especial (!@#$%&*)
> # Digite outra senha:
> ```

---

> **Exercício 3 — Gerenciador de Lista de IPs:** Crie um programa com menu interativo (usando `while True`) que gerencie uma lista de endereços IP. O menu deve ter as opções: [1] Adicionar IP, [2] Remover IP, [3] Listar todos, [4] Buscar IP, [5] Sair. Não permita IPs duplicados na lista. Na busca, informe se o IP foi encontrado e em qual posição. Use `break` para sair do loop quando o usuário escolher a opção 5.
>
> ```python
> # Lista inicial para teste:
> ips = ["192.168.1.1", "10.0.0.5", "172.16.0.3"]
>
> # Sequência de teste:
> # [1] Adicionar: "192.168.1.10" → "IP adicionado!"
> # [1] Adicionar: "10.0.0.5"    → "IP já existe na lista!"
> # [4] Buscar: "172.16.0.3"     → "IP encontrado na posição 3"
> # [4] Buscar: "8.8.8.8"        → "IP não encontrado"
> # [2] Remover: "10.0.0.5"      → "IP removido!"
> # [3] Listar                   → exibe todos os IPs numerados
> # [5] Sair                     → "Encerrando..."
> ```

---

> **Exercício 4 — Análise de Notas com Tuplas:** Crie um programa que receba as notas de 5 alunos (nome e nota) e armazene cada par como uma tupla dentro de uma lista. Depois, usando laços, calcule e exiba: a maior nota e o nome do aluno, a menor nota e o nome do aluno, a média da turma, e quais alunos estão acima da média. Use `for` para percorrer a lista.
>
> ```python
> # Dados para teste (podem ser digitados ou hardcoded):
> alunos = [
>     ("Carlos", 8.5),
>     ("Ana", 9.2),
>     ("Bruno", 6.0),
>     ("Diana", 7.8),
>     ("Eduardo", 4.5),
> ]
>
> # Saída esperada:
> # === Relatório de Notas ===
> # Maior nota: Ana - 9.2
> # Menor nota: Eduardo - 4.5
> # Média da turma: 7.2
> #
> # Alunos acima da média:
> # - Carlos: 8.5
> # - Ana: 9.2
> # - Diana: 7.8
> ```

---

> **Exercício 5 — Contador de Palavras com Dicionário:** Crie um programa que receba um texto do usuário e conte quantas vezes cada palavra aparece, armazenando em um dicionário (palavra como chave, contagem como valor). Converta tudo para minúsculo antes de contar. Ao final, exiba as palavras ordenadas pela frequência (da mais frequente para a menos frequente) e destaque a palavra mais usada.
>
> ```python
> # Texto para teste:
> texto = "o gato viu o rato e o rato viu o gato e o gato correu"
>
> # Saída esperada:
> # === Contagem de Palavras ===
> # "o"      → 6 vezes
> # "gato"   → 3 vezes
> # "rato"   → 2 vezes
> # "viu"    → 2 vezes
> # "e"      → 2 vezes
> # "correu" → 1 vez
> #
> # Palavra mais frequente: "o" (6 vezes)
> # Total de palavras únicas: 6
> ```

---

> **Exercício 6 — Blacklist de IPs com Sets:** Crie um programa que compare dois sets: um com IPs que acessaram o servidor e outro com uma blacklist de IPs maliciosos. Usando operações de conjuntos, descubra e exiba: quais IPs maliciosos foram detectados (interseção), quais IPs são seguros (diferença), quais IPs da blacklist não apareceram (diferença inversa) e o total de IPs únicos considerando ambas as listas (união). Exiba os resultados formatados.
>
> ```python
> acessos = {"192.168.1.10", "10.0.0.5", "185.220.101.1", "172.16.0.3",
>            "192.168.1.20", "91.240.118.172", "10.0.0.12", "45.33.32.156"}
>
> blacklist = {"185.220.101.1", "45.33.32.156", "91.240.118.172",
>              "23.94.5.100", "104.244.72.115"}
>
> # Saída esperada:
> # === Relatório de Segurança ===
> # IPs maliciosos detectados (3):
> #   - 185.220.101.1
> #   - 45.33.32.156
> #   - 91.240.118.172
> #
> # IPs seguros (5):
> #   - 192.168.1.10
> #   - 10.0.0.5
> #   - 172.16.0.3
> #   - 192.168.1.20
> #   - 10.0.0.12
> #
> # IPs da blacklist não detectados (2):
> #   - 23.94.5.100
> #   - 104.244.72.115
> #
> # Total de IPs únicos: 10
> ```

---

> **Exercício 7 — Calculadora Segura com Exceções:** Crie uma calculadora que opere em loop (`while True`) pedindo dois números e uma operação (+, -, *, /). O programa deve tratar com `try/except`: entrada não numérica (`ValueError`), divisão por zero (`ZeroDivisionError`) e operação inválida. Use `else` para exibir o resultado quando não houver erro e `finally` para exibir "Operação processada." sempre. O usuário pode digitar "sair" para encerrar.
>
> ```python
> # Sequência de teste:
> # Número 1: abc     → "Erro: Digite apenas números!"
> # Número 1: 10
> # Número 2: 0
> # Operação: /       → "Erro: Divisão por zero!"
> # Número 1: 10
> # Número 2: 3
> # Operação: /       → "Resultado: 3.33"
> # Número 1: 5
> # Número 2: 3
> # Operação: %       → "Erro: Operação '%' não suportada. Use +, -, * ou /"
> # Número 1: sair    → "Encerrando calculadora."
>
> # Cada interação deve exibir ao final:
> # "Operação processada." (via finally)
> ```

---

> **Exercício 8 — Inventário de Ativos com CRUD:** Crie um programa que gerencie um inventário de ativos de rede usando uma lista de dicionários. Cada ativo tem: nome, tipo (servidor/estação/switch/roteador), IP e status (ativo/inativo). O programa deve ter menu com: [1] Cadastrar ativo, [2] Listar ativos, [3] Buscar por IP, [4] Alterar status, [5] Remover ativo, [6] Sair. Trate com exceções entradas inválidas (ex: IP duplicado, ativo não encontrado). Use `for` para buscas e listagens.
>
> ```python
> # Dados iniciais:
> ativos = [
>     {"nome": "SRV-WEB01", "tipo": "servidor", "ip": "192.168.1.10", "status": "ativo"},
>     {"nome": "PC-RH03", "tipo": "estacao", "ip": "192.168.1.45", "status": "ativo"},
>     {"nome": "SW-CORE01", "tipo": "switch", "ip": "192.168.1.1", "status": "inativo"},
> ]
>
> # Sequência de teste:
> # [1] Cadastrar: nome="SRV-DB01", tipo="servidor", ip="192.168.1.20" → "Cadastrado!"
> # [1] Cadastrar: ip="192.168.1.10" → "Erro: IP já cadastrado!"
> # [3] Buscar: ip="192.168.1.45"  → exibe dados do PC-RH03
> # [3] Buscar: ip="8.8.8.8"       → "Ativo não encontrado"
> # [4] Alterar: ip="192.168.1.1", novo status="ativo" → "Status atualizado!"
> # [5] Remover: ip="192.168.1.45" → "Ativo removido!"
> # [2] Listar → exibe todos os ativos formatados
> ```

---

> **Exercício 9 — Analisador de Logs de Segurança:** Crie um programa que analise uma lista de logs (strings), extraindo informações com manipulação de strings e armazenando em dicionários. Para cada log: extraia o nível (INFO/WARNING/ERROR), o IP de origem e a mensagem. Conte os eventos por nível, identifique o IP com mais erros e gere um relatório. Use `for`, dicionários e `try/except` para tratar logs malformados.
>
> ```python
> logs = [
>     "[2025-02-20 08:15:01] [INFO] Login ok - IP: 192.168.1.10",
>     "[2025-02-20 08:15:03] [WARNING] Area restrita - IP: 10.0.0.5",
>     "[2025-02-20 08:15:10] [ERROR] Falha auth - IP: 185.220.101.1",
>     "[2025-02-20 08:15:15] [INFO] Arquivo acessado - IP: 192.168.1.10",
>     "[2025-02-20 08:15:22] [ERROR] Conexao recusada - IP: 185.220.101.1",
>     "[2025-02-20 08:15:30] [WARNING] Certificado SSL - IP: 172.16.0.3",
>     "[2025-02-20 08:15:35] [ERROR] Falha auth - IP: 10.0.0.5",
>     "log malformado sem formato correto",
>     "[2025-02-20 08:15:45] [ERROR] Timeout - IP: 185.220.101.1",
>     "[2025-02-20 08:15:50] [WARNING] CPU alta - IP: 192.168.1.20",
>     "[2025-02-20 08:16:01] [ERROR] Falha auth - IP: 185.220.101.1",
>     "[2025-02-20 08:16:05] [INFO] Firewall ok - IP: 192.168.1.10",
> ]
>
> # Saída esperada:
> # === Relatório de Logs ===
> # INFO:    3 eventos
> # WARNING: 3 eventos
> # ERROR:   4 eventos
> # Logs malformados: 1
> #
> # IP com mais erros: 185.220.101.1 (3 erros)
> #
> # Detalhamento de erros:
> #   185.220.101.1 → 3 erros
> #   10.0.0.5      → 1 erro
> ```

---

> **Exercício 10 (Desafio) — Sistema Completo de Gerenciamento de Senhas:** Crie um programa que combine todos os conceitos das aulas 6-8 em um sistema de gerenciamento de senhas. O programa deve usar um `while True` com menu: [1] Cadastrar senha (serviço + senha), [2] Listar serviços, [3] Buscar senha por serviço, [4] Gerar senha aleatória, [5] Avaliar força de todas as senhas, [6] Exportar relatório, [7] Sair.
>
> Requisitos:
> - Armazene as senhas em um **dicionário** (serviço como chave, senha como valor)
> - **Não permita serviços duplicados** (trate com exceção ou validação)
> - Ao cadastrar, **avalie a força** da senha (fraca/média/forte) usando `for` para verificar critérios
> - **Gerar senha aleatória** de tamanho N usando `for` + `random.choice` com letras, números e símbolos
> - **Avaliar força** deve percorrer todas as senhas do dicionário com `for` e classificar cada uma
> - **Exportar relatório** deve usar `try/except` para tratar erro de escrita em arquivo
> - Trate todas as entradas inválidas com `try/except`
>
> ```python
> import random
>
> # Dados iniciais:
> senhas = {
>     "gmail": "MinhaS3nha!",
>     "github": "Dev@2024Seguro",
>     "banco_dados": "db123",
> }
>
> # Critérios de força:
> # Fraca:  < 8 caracteres
> # Média:  8+ chars com letras e números (sem especial)
> # Forte:  8+ chars com maiúscula, minúscula, número e especial
>
> # Caracteres para geração aleatória:
> caracteres = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%&*"
>
> # Sequência de teste:
> # [1] Cadastrar: "linkedin" / "Minha@Senha1" → "Cadastrado! Força: Forte"
> # [1] Cadastrar: "gmail" / "outra"           → "Erro: Serviço já cadastrado!"
> # [4] Gerar: tamanho=16                      → exibe senha aleatória gerada
> # [5] Avaliar todas:
> #     gmail:      "MinhaS3nha!"     → Forte
> #     github:     "Dev@2024Seguro"  → Forte
> #     banco_dados: "db123"          → Fraca
> #     linkedin:   "Minha@Senha1"    → Forte
> # [6] Exportar → salva relatório em "senhas_relatorio.txt"
> #     → "Relatório exportado com sucesso!"
> #     (se der erro de escrita: "Erro ao exportar: [mensagem]")
> # [7] Sair → "Encerrando..."
> ```
