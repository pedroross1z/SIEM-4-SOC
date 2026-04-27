# CODING FOR SECURITY — Apostila de Programação em Python — 1º Semestre

| | |
|---|---|
| **Disciplina:** | Coding for Security |
| **Professor:** | Fabio Bara |
| **Carga Horária:** | 4 horas/semana |
| **Período:** | 1º Semestre |
| **Referências:** | Python Crash Course (Eric Matthes) |
| | Automate the Boring Stuff with Python (Al Sweigart) |

---

## Sumário

- [Aula 1 — Apresentação e Objetivos](#aula-1--apresentação-e-objetivos)
- [Aula 2 — Instalação do Python, VS Code, Workspace e PIP](#aula-2--instalação-do-python-vs-code-workspace-e-pip)
- [Aula 3 — Entrada/Saída e Variáveis](#aula-3--entradasaída-e-variáveis)
- [Aula 4 — Condicionais: if e elif](#aula-4--condicionais-if-e-elif)
- [Aula 5 — Check Point 01](#aula-5--check-point-01)
- [Aula 6 — Repetição: for e while](#aula-6--repetição-for-e-while)
- [Aula 7 — Listas, Tuplas e Dicionários](#aula-7--listas-tuplas-e-dicionários)
- [Aula 8 — Tratamento de Exceções](#aula-8--tratamento-de-exceções)
- [Aula 9 — Check Point 02](#aula-9--check-point-02)
- [Aula 10 — Funções](#aula-10--funções)
- [Aula 11 — Módulos e Comandos do Sistema](#aula-11--módulos-e-comandos-do-sistema)
- [Aula 12 — Escrita e Leitura de Arquivos](#aula-12--escrita-e-leitura-de-arquivos)
- [Aula 13 — Sockets](#aula-13--sockets)
- [Aula 14 — Requests e JSON](#aula-14--requests-e-json)
- [Aula 15 — Check Point 03](#aula-15--check-point-03)

---

## Aula 1 — Apresentação e Objetivos

### 1.1 Sobre a Disciplina

Bem-vindo à disciplina **Coding for Security**! Neste curso, você aprenderá a programar em Python com foco em segurança da informação. Python é uma das linguagens mais utilizadas no mundo da cibersegurança, sendo empregada para automação de tarefas, análise de vulnerabilidades, desenvolvimento de ferramentas de segurança, testes de penetração e muito mais.

A linguagem Python foi criada por Guido van Rossum e lançada pela primeira vez em 1991. Sua filosofia de design enfatiza a legibilidade do código, utilizando indentação significativa como parte da sintaxe.

### 1.2 Por Que Python?

- **Simplicidade:** Sintaxe limpa e legível, ideal para iniciantes.
- **Versatilidade:** Web, automação, análise de dados, IA e segurança.
- **Comunidade:** Milhares de bibliotecas disponíveis.
- **Segurança:** Nmap, Scapy e Metasploit possuem integração com Python.
- **Mercado de trabalho:** Grande demanda em cibersegurança.

### 1.3 Objetivos do Semestre

Ao final deste semestre, você será capaz de:

- Configurar um ambiente de desenvolvimento Python completo
- Escrever programas com variáveis, operadores e estruturas de controle
- Trabalhar com listas, tuplas e dicionários
- Criar e utilizar funções
- Manipular arquivos de texto
- Tratar exceções e erros
- Utilizar módulos e bibliotecas externas
- Programar com sockets para comunicação em rede
- Fazer requisições HTTP e manipular dados JSON

### 1.4 Materiais de Referência

- **Python Crash Course, 2ª Edição** — Eric Matthes
- **Automate the Boring Stuff with Python, 2ª Edição** — Al Sweigart

### 1.5 Avaliação

- **Check Points (3):** Semanas 5, 9 e 15
- **Provas Semestrais:** Semanas 16 e 17
- **Participação:** Presença e participação ativa

---

## Aula 2 — Instalação do Python, VS Code, Workspace e PIP

### 2.1 Instalando o Python

#### Windows

1. Acesse **https://python.org/downloads** e clique em "Download Python 3.x.x" (versão mais recente).
2. Execute o instalador baixado (`python-3.x.x-amd64.exe`).
3. **IMPORTANTE:** Na primeira tela do instalador, marque a opção **"Add python.exe to PATH"** (checkbox na parte inferior).
4. Clique em **"Install Now"** para instalação padrão, ou em "Customize installation" se quiser alterar o diretório.
5. Aguarde a instalação concluir e clique em "Close".
6. Para verificar, abra o **Prompt de Comando** (tecla Windows, digite `cmd`, Enter) e execute:

```bash
python --version
```

Saída esperada:
```
Python 3.12.x
```

Verifique também o PIP:
```bash
pip --version
```

> ⚠️ É fundamental marcar "Add python.exe to PATH" durante a instalação. Sem isso, o Windows não encontrará o comando `python` no terminal. Caso tenha esquecido, desinstale e reinstale marcando a opção, ou adicione manualmente o caminho `C:\Users\SeuUsuario\AppData\Local\Programs\Python\Python3x\` nas variáveis de ambiente do sistema.

#### macOS/Linux

```bash
# macOS
brew install python3

# Ubuntu/Debian
sudo apt update && sudo apt install python3 python3-pip
```

### 2.2 Visual Studio Code

- Acesse **https://code.visualstudio.com** e baixe o instalador.
- Instale a extensão **Python** da Microsoft.

#### Criando um Workspace

Crie uma pasta `C:\CodingForSecurity`. No VS Code: File > Open Folder.

#### Primeiro Programa

```python
# hello.py
print("Olá, Mundo!")
print("Bem-vindo ao Coding for Security!")
```

### 2.3 PIP — Gerenciador de Pacotes

```bash
pip install nome_do_pacote
pip list
pip install --upgrade nome_do_pacote
pip uninstall nome_do_pacote
```

### 2.4 Terminal Interativo

```python
>>> 2 + 2
4
>>> print('Olá!')
Olá!
>>> exit()
```

## Exercício: 
1) Instale Python 3 e VS Code. 
2) Crie um workspace. 
3) Crie um arquivo que imprima seu nome. 
4) Instale o pacote `requests` via PIP.

---

## Aula 3 — Entrada/Saída e Variáveis


### 3.1 Objetos e Classes

Para entendermos as variveis no Python, precisamos entender o que é um objeto e uma classe

Um objeto é uma estrutura que agrupa dados (atributos) e comportamentos (métodos) em uma única entidade. 
Pense nele como uma "coisa" que existe na memória do programa, que tem características e sabe fazer coisas.
Uma classe é o molde que define como esses objetos são criados — quais atributos eles terão e quais métodos poderão executar. 
A classe é a planta da casa; o objeto é a casa construída.

Em Java, isso fica bem visível:

```Java
// String é uma classe; "hello" é um objeto dessa classe
String nome = new String("hello");
nome.length();      // funciona, porque é objeto

// int é primitivo — não é objeto, não tem métodos
int x = 42;
x.toString();       // ERRO! Primitivo não tem métodos

// Integer é a classe wrapper — agora sim é objeto
Integer y = 42;
y.toString();       // funciona
```

Em Python, como tudo é objeto, não existe essa separação. Cada valor já nasce como instância de uma classe:

```python
x = 42        # x é um objeto da classe int
x.bit_length()      # funciona! Retorna 6

nome = "hello"      # objeto da classe str
nome.upper()        # funciona! Retorna "HELLO"

ativo = True        # objeto da classe bool
type(ativo)         # <class 'bool'>
```

Você pode inclusive verificar que todo valor em Python é instância de alguma classe usando type() — não há exceções.

Isso vale para todos os tipos em Python: uma string "hello" é um objeto da classe str, o valor True é um objeto da classe bool, 
até o None é um objeto (a única instância da classe NoneType). Não existe nenhum valor em Python que não seja um objeto.
Na prática, para quem está começando, os tipos int, float, str, bool e NoneType se comportam de forma simples e direta, 
semelhante aos primitivos de outras linguagens. A diferença é que, por baixo dos panos, Python trata todos eles como objetos completos — 
o que dá mais flexibilidade e uniformidade à linguagem, ao custo de um pouco mais de uso de memória.


### 3.2 Variáveis em Python

```python
mensagem = "Olá, Python!"
print(mensagem)

numero = 42
preco = 19.99
ativo = True
nome = 'Maria'

print(numero)
print(preco)
print(ativo)
print(nome)
```

#### Regras para Nomes

- Podem conter letras, números e underscores (_)
- Devem começar com letra ou underscore
- Não podem ser palavras reservadas
- Case-sensitive: `Nome` ≠ `nome`

#### Tipos de Dados

| Tipo | Descrição | Exemplo |
|------|-----------|---------|
| `int` | Inteiros | `42, -10, 0` |
| `float` | Decimais | `3.14, -0.5` |
| `str` | Texto | `"Olá", 'Python'` |
| `bool` | Booleano | `True, False` |
| `NoneType` | Ausência de valor | `None` |

```python
idade = 25
print(type(idade))    # <class 'int'>

nome = "Carlos"
print(type(nome))     # <class 'str'>
```

### 3.3 Strings e f-strings

```python
nome = "João"
idade = 20

print(f"Meu nome é {nome} e tenho {idade} anos.")
print(f"No próximo ano terei {idade + 1} anos.")

print(nome.upper())   # JOÃO
print(nome.lower())   # joão
print(len(nome))      # 4
```

### 3.4 Operadores

| Operador | Descrição | Exemplo | Resultado |
|----------|-----------|---------|-----------|
| `+` | Adição | `3 + 2` | `5` |
| `-` | Subtração | `10 - 4` | `6` |
| `*` | Multiplicação | `3 * 4` | `12` |
| `/` | Divisão | `10 / 3` | `3.333...` |
| `//` | Divisão inteira | `10 // 3` | `3` |
| `%` | Módulo | `10 % 3` | `1` |
| `**` | Exponenciação | `2 ** 8` | `256` |

### 3.5 Entrada com input()

```python
nome = input("Digite seu nome: ")
print(f"Olá, {nome}!")

idade = int(input("Digite sua idade: "))
altura = float(input("Digite sua altura: "))
```

### 3.6 Conversão de Tipos

```python
texto = "42"
numero = int(texto)      # 42

texto = "3.14"
decimal = float(texto)   # 3.14

idade = 25
texto = str(idade)       # "25"
```

## Exercício: 

1) Peça nome, idade e cidade e exiba mensagem formatada. 
2) Calculadora simples. 
3) Calcule o IMC.

---

## Aula 4 — Condicionais: if e elif

### 4.1 Decisões com if

```python
idade = 18
if idade >= 18:
    print("Você é maior de idade.")
    print("Pode acessar o sistema.")
```

#### Operadores de Comparação

| Operador | Descrição |
|----------|-----------|
| `==` | Igual a |
| `!=` | Diferente de |
| `>` | Maior que |
| `<` | Menor que |
| `>=` | Maior ou igual |
| `<=` | Menor ou igual |

### 4.2 if-else

```python
idade = int(input("Digite sua idade: "))
if idade >= 18:
    print("Maior de idade. Acesso permitido.")
else:
    print("Menor de idade. Acesso negado.")
```

### 4.3 if-elif-else

```python
nota = float(input("Digite sua nota: "))
if nota >= 9.0:
    conceito = "A"
elif nota >= 7.0:
    conceito = "B"
elif nota >= 5.0:
    conceito = "C"
else:
    conceito = "F"
print(f"Nota: {nota} - Conceito: {conceito}")
```

### 4.4 Operadores Lógicos

| Operador | Descrição | Exemplo |
|----------|-----------|---------|
| `and` | Ambas verdadeiras | `x > 0 and x < 100` |
| `or` | Pelo menos uma | `x < 0 or x > 100` |
| `not` | Inverte | `not (x > 0)` |

### 4.5 Exemplo: Sistema de Login

```python
usuario = input("Usuário: ")
senha = input("Senha: ")

if usuario == "admin" and senha == "Cyber@2024":
    print("Login realizado com sucesso!")
    print("Bem-vindo, Administrador.")
elif usuario == "admin":
    print("Senha incorreta!")
else:
    print("Usuário não cadastrado!")
```

## Exercício: 

1) Positivo, negativo ou zero. 
2) Classifique triângulos. 
3) Login com 3 tentativas.

---

## Aula 5 — Check Point 01

### Revisão (Aulas 1-4)

- **Ambiente:** Python, VS Code, PIP
- **Variáveis e tipos:** int, float, str, bool
- **Entrada/Saída:** input(), print(), f-strings
- **Operadores:** aritméticos, comparação, lógicos
- **Condicionais:** if, elif, else

## Exercício: 

> 1) **Calculadora de Desconto:** Receba valor e porcentagem, calcule preço final.
> 2) **Verificador de Senha Forte:** Mínimo 8 caracteres e pelo menos um número.
> 3) **Conversor de Temperatura:** Celsius ↔ Fahrenheit ↔ Kelvin.

---

## Aula 6 — Repetição: for e while

### 6.1 Laços (Loops)
Um laço (ou loop) é uma estrutura que permite repetir um bloco de código múltiplas vezes. Sem laços, 
se você quisesse imprimir os números de 1 a 1000, precisaria escrever 1000 linhas de print().
Com um laço, resolve em duas linhas.

Laços existem para resolver um problema fundamental da programação: automação de tarefas repetitivas. 
Em segurança, isso é especialmente importante — você não vai testar 65.535 portas de um servidor manualmente, 
nem analisar milhares de linhas de log uma por uma.
Existem duas situações principais que pedem um laço:

Você sabe quantas vezes quer repetir — use for. 
Exemplo: percorrer uma lista de IPs, iterar sobre cada linha de um arquivo.

Você não sabe quantas vezes, mas sabe quando parar — use while. 
Exemplo: pedir senha até o usuário acertar, monitorar um serviço até ele cair.

### 6.2 Loop Infinito
Um loop infinito acontece quando a condição de parada nunca é satisfeita — o programa fica preso repetindo para sempre:

```python
# Loop infinito acidental (esqueceu de incrementar)
contador = 1
while contador <= 10:
    print(contador)
    # Faltou: contador += 1
    # contador nunca muda, então sempre será <= 10
```

Nem todo loop infinito é um erro. Em servidores e sistemas de monitoramento, 
loops infinitos intencionais são comuns — um servidor web, por exemplo, precisa ficar escutando conexões indefinidamente:

```python
while True:
    conexao = servidor.accept()
    processar(conexao)
```

A diferença entre um loop infinito intencional e um bug é o controle: o intencional tem mecanismos de saída (break, sinais do sistema operacional), 
enquanto o acidental trava o programa.


### 6.3 O Laço for

```python
frutas = ["maçã", "banana", "laranja"]
for fruta in frutas:
    print(f"Eu gosto de {fruta}")

for letra in "Python":
    print(letra)
```

#### A Função range()

```python
for i in range(5):         # 0,1,2,3,4
    print(i)

for i in range(1, 6):      # 1,2,3,4,5
    print(i)

for i in range(0, 10, 2):  # 0,2,4,6,8
    print(i)

for i in range(10, 0, -1): # 10,9,...,1
    print(i)
```

### 6.4 O Laço while

```python
contador = 1
while contador <= 5:
    print(f"Contagem: {contador}")
    contador += 1

senha = ""
while senha != "abc123":
    senha = input("Digite a senha: ")
print("Acesso liberado!")
```

> ⚠️ Cuidado com loops infinitos!

### 6.5 break e continue

```python
# break - interrompe o loop
for i in range(10):
    if i == 5:
        break
    print(i)  # 0,1,2,3,4

# continue - pula para próxima iteração
for i in range(10):
    if i % 2 == 0:
        continue
    print(i)  # 1,3,5,7,9
```

### 6.6 Exemplo: Scanner de Portas (Conceito)

```python
portas_abertas = [22, 80, 443, 8080]
print("=== Scanner de Portas (Simulação) ===")
for porta in range(1, 1025):
    if porta in portas_abertas:
        print(f"Porta {porta}: ABERTA")
```

## Exercício: 

1) Números primos entre 1-100. 
2) Jogo de adivinhação. 
3) Força bruta de senhas de 4 dígitos.

---

## Aula 7 — Estruturas de Dados: Listas, Tuplas, Dicionários e Sets

Python oferece quatro estruturas de dados fundamentais, e cada uma existe para resolver um tipo diferente de problema. 
Escolher a estrutura certa impacta diretamente na performance e na clareza do seu código.

### 7.1 Listas (list)

Uma lista é uma coleção ordenada e mutável de elementos. Ordenada significa que os itens mantêm a posição em que foram inseridos. 
Mutável significa que você pode adicionar, remover e alterar elementos depois de criar a lista.


```python
# Exemplo basico
numeros = [1, 2, 3, 4, 5]
nomes = ["Ana", "Bruno", "Carlos"]

print(nomes[0])     # Ana
print(nomes[-1])    # Carlos
print(numeros[1:3]) # [2, 3]
```

```python
# Exemplo de segurança
ips = ["192.168.1.1", "10.0.0.1", "172.16.0.1"]
ips.append("192.168.1.2")    # Adiciona ao final
ips[0] = "192.168.1.100"     # Altera o primeiro elemento
del ips[1]  
```

Internamente, a lista é implementada como um array dinâmico. Isso significa que acessar um elemento por índice (lista[5]) é muito rápido — O(1), ou seja, leva o mesmo tempo independente do tamanho da lista. Porém, buscar se um elemento existe ("10.0.0.1" in ips) é O(n) — Python precisa verificar cada elemento um por um. Com 10 itens não faz diferença, mas com 10 milhões faz.
Quando usar: quando a ordem importa, quando você precisa modificar os dados frequentemente, quando acessa elementos por posição.

#### Métodos de Lista

```python
lista = [3, 1, 4, 1, 5, 9]
lista.append(2)        # Adiciona ao final
lista.insert(0, 0)     # Insere na posição
lista.remove(1)        # Remove primeiro 1
elemento = lista.pop() # Remove e retorna último
lista.sort()           # Ordena
print(len(lista))      # Tamanho
print(4 in lista)      # True
```

#### List Comprehension

```python
quadrados = [x ** 2 for x in range(10)]
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

pares = [x for x in range(20) if x % 2 == 0]
```

### 7.2 Tuplas

Uma tupla é uma coleção ordenada e imutável. Uma vez criada, não pode ser alterada — não dá para adicionar, remover nem modificar elementos.

```python
coordenadas = (10.5, 20.3, 5.0)  # Tupla de coordenadas (latitude, longitude, altitude)
print(coordenadas[0])  # 10.5

coordenadas[0] = 0.0   # ERRO! Tupla é imutável

# Desempacotamento
latitude, longitude, altitude = coordenadas
print(latitude)
print(longitude)
print(altitude)

```

A imutabilidade parece uma limitação, mas na verdade é uma garantia de segurança. Quando você passa uma tupla para uma função, 
tem certeza de que ninguém vai alterar os dados originais. Isso evita bugs sutis em programas grandes.

## Comparação com lista:

|    Característica   |     Lista     |      Tupla      |
|---------------------|---------------|-----------------|
|    Mutável          |      Sim      |       Não       | 
| Performance         |    Ligeiramente mais lenta | Ligeiramente mais rápida |
|Memória | Usa mais | Usa menos | 
| Pode ser chave de dicionário | Não | Sim |
| Caso de uso | Dados que mudam | Dados fixos |

Quando usar: coordenadas, configurações que não devem mudar, retorno de múltiplos valores de uma função, chaves compostas em dicionários.


### 7.3 Dicionários (dict)

Um dicionário é uma coleção de pares chave-valor. Essa é a estrutura mais importante para entender bem, 
porque ela resolve um problema que listas não resolvem de forma eficiente: busca rápida por identificador.
Imagine que você tem 100.000 usuários e precisa encontrar o email do usuário "carlos". Com uma lista, 
teria que percorrer item por item até encontrar — no pior caso, 100.000 comparações. Com um dicionário, 
a busca é praticamente instantânea, independente de quantos elementos existam.

```python
# Exemplo Basico
usuario = {
    "nome": "Carlos",
    "idade": 25,
    "email": "carlos@email.com",
    "ativo": True
}

print(usuario["nome"])  # Carlos
usuario["idade"] = 26   # Modificar
del usuario["ativo"]    # Remover

for chave, valor in usuario.items():
    print(f"{chave}: {valor}")
```

```python 
# Exemplo Avançado
usuarios = {
    "carlos": {"email": "carlos@empresa.com", "nivel": 3},
    "ana": {"email": "ana@empresa.com", "nivel": 5},
    "bruno": {"email": "bruno@empresa.com", "nivel": 1}
}

# Busca direta pela chave — O(1), instantâneo
print(usuarios["carlos"]["email"])
````

Isso acontece porque, internamente, o dicionário usa uma hash table. Quando você usa uma chave, 
Python calcula um hash (um número único derivado da chave) e usa esse hash como endereço direto na memória. 
É como a diferença entre procurar um nome em uma lista de 100.000 nomes (lendo um por um) versus procurar em um índice alfabético que te leva direto à página certa.

## Performance comparada:

|    Operação   |     Lista     |      Dicionário      |
|---------------|---------------|----------------------|
|    Acessar por índice/chave          |      O(1)      |       O(1)       | 
| Buscar se elemento existe         |   O(n) — lento  | O(1) — rápido |
| Inserir no final | O(1) | O(1) | 
| Remover por valor | O(n) | O(1) |

## Regra importante 
 
As chaves de um dicionário devem ser imutáveis (strings, números, tuplas). Listas não podem ser chaves, 
justamente porque são mutáveis — se a chave mudasse depois de inserida, o hash mudaria e o dicionário perderia a referência.

Quando usar: sempre que precisar buscar dados por um identificador (nome, ID, IP, CVE), mapear relações entre dados, contar ocorrências, caches.


```pytjon 
# Funciona — chaves são strings (imutáveis)
config = {"host": "localhost", "porta": 8080}

# Funciona — tupla como chave
localizacoes = {(23.55, -46.63): "São Paulo", (40.71, -74.00): "New York"}

# ERRO — lista não pode ser chave
errado = {[1, 2, 3]: "valor"}  # TypeError: unhashable type: 'list'
```

### 7.4 Exemplo: Banco de Vulnerabilidades

```python
vulnerabilidades = [
    {"id": "CVE-2024-001", "tipo": "SQL Injection",
     "severidade": "Alta", "corrigida": False},
    {"id": "CVE-2024-002", "tipo": "XSS",
     "severidade": "Média", "corrigida": True},
]

for vuln in vulnerabilidades:
    if not vuln["corrigida"]:
        print(f"{vuln['id']} - {vuln['tipo']} [{vuln['severidade']}]")
```

### 7.5 Set (set)
Um set é uma coleção não ordenada de elementos únicos. Ele não permite duplicatas e não mantém ordem de inserção. 
Assim como o dicionário, usa hash table internamente, então buscar se um elemento existe é O(1).

```python
# Criando um set
portas_abertas = {22, 80, 443, 8080}
portas_suspeitas = {4444, 8080, 31337, 443}

# Duplicatas são ignoradas automaticamente
numeros = {1, 2, 2, 3, 3, 3}
print(numeros)  # {1, 2, 3}

# Verificar se existe — O(1), muito rápido
print(80 in portas_abertas)  # True
```

O grande poder dos sets está nas operações de conjunto, que vêm direto da teoria de conjuntos da matemática:

```python 
# Interseção — portas que aparecem em ambos
comuns = portas_abertas & portas_suspeitas
print(comuns)  # {443, 8080}

# União — todas as portas juntas (sem duplicar)
todas = portas_abertas | portas_suspeitas
print(todas)  # {22, 80, 443, 4444, 8080, 31337}

# Diferença — portas abertas que NÃO são suspeitas
seguras = portas_abertas - portas_suspeitas
print(seguras)  # {22, 80}

# Diferença simétrica — portas que estão em um OU outro, mas não em ambos
exclusivas = portas_abertas ^ portas_suspeitas
print(exclusivas)  # {22, 80, 4444, 31337}
```

Em segurança, sets são extremamente úteis. Exemplo prático — comparar IPs de uma blacklist:

```python 
ips_da_rede = {"192.168.1.10", "10.0.0.5", "185.220.101.1", "192.168.1.20"}
blacklist = {"185.220.101.1", "45.33.32.156", "91.240.118.172"}

# Quais IPs da rede estão na blacklist?
ameacas = ips_da_rede & blacklist
print(f"IPs maliciosos detectados: {ameacas}")
# {'185.220.101.1'}
```

Com uma lista, essa comparação seria O(n×m) — lenta para listas grandes. 
Com sets, é O(min(n,m)) — muito mais eficiente.
Existe também o frozenset — um set imutável, que pode ser usado como chave de dicionário (assim como a tupla é a versão imutável da lista).

## Resumo Comparativo

Estrutura | Ordenada | Mutável | Duplicatas | Busca | Quando usar | 
--------- | -------- | ------- | ---------- | ----- | ----------- | 
list | Sim | Sim | Sim | O(n) | Sequências que mudam | 
tuple | Sim | Não | Sim | O(n) | Dados fixos, chaves compostas | 
dict | Sim* | Sim | Chaves únicas | O(1) | Busca por identificador | 
set | Não | Sim | Não | O(1) | Elementos únicos, operações de conjunto | 
frozenset | Não | Não | Não | O(1) | Set imutável, chave de dicionário | 

* Dicionários mantêm ordem de inserção a partir do Python 3.7.


## Exercício: 
1) Agenda Telefônica: Crie uma agenda usando dicionário com menu para: adicionar, buscar, remover, listar e atualizar contatos. Trate casos de contato inexistente e duplicado. Use estes dados iniciais para testar:
```python
agenda = {
    "Ana Silva": "(11) 98765-4321",
    "Bruno Costa": "(11) 91234-5678",
    "Carlos Souza": "(21) 99876-5432",
    "Diana Lima": "(31) 97654-3210"
}
```

2) IPs vs Blacklist: Compare os IPs que acessaram seu servidor contra uma blacklist. Identifique os maliciosos, conte quantas requisições cada um fez, e classifique a ameaça (crítica >100, alta >50, média >10, baixa). Dados para teste:
```python
requisicoes = [
    "192.168.1.10", "185.220.101.1", "10.0.0.5", "185.220.101.1",
    "91.240.118.172", "192.168.1.10", "185.220.101.1", "10.0.0.5",
    "45.33.32.156", "185.220.101.1", "91.240.118.172", "192.168.1.20",
    "185.220.101.1", "45.33.32.156", "185.220.101.1", "91.240.118.172",
]

blacklist = {"185.220.101.1", "45.33.32.156", "91.240.118.172"}
```

3) Inventário de Ativos: Crie um sistema de inventário com lista de dicionários. Permita cadastrar, listar com filtro (por tipo/status), buscar por IP e gerar relatório de ativos inativos há mais de 30 dias. Salve em JSON. Dados iniciais:
```python

ativos = [
    {"nome": "SRV-WEB01", "tipo": "servidor", "ip": "192.168.1.10",
     "so": "Ubuntu 22.04", "status": "ativo", "ultimo_acesso": "2025-02-20"},
    {"nome": "PC-RH03", "tipo": "estacao", "ip": "192.168.1.45",
     "so": "Windows 11", "status": "ativo", "ultimo_acesso": "2025-01-05"},
    {"nome": "SW-CORE01", "tipo": "switch", "ip": "192.168.1.1",
     "so": "Cisco IOS", "status": "inativo", "ultimo_acesso": "2024-11-15"},
    {"nome": "SRV-DB01", "tipo": "servidor", "ip": "192.168.1.20",
     "so": "Debian 12", "status": "ativo", "ultimo_acesso": "2025-02-19"},
]

```

4) Análise de Logs com Sets: Você recebeu dois logs de acesso (ontem e hoje) e uma blacklist. Descubra: IPs novos de hoje, IPs que pararam de acessar, IPs presentes nos dois dias, e ameaças detectadas em cada dia. Dados para teste:

```python
ips_ontem = {
    "192.168.1.10", "10.0.0.5", "172.16.0.3", "192.168.1.20",
    "10.0.0.12", "185.220.101.1", "192.168.1.45", "172.16.0.7"
}

ips_hoje = {
    "192.168.1.10", "10.0.0.5", "192.168.1.20", "45.33.32.156",
    "10.0.0.50", "172.16.0.3", "91.240.118.172", "192.168.1.80"
}

blacklist = {"185.220.101.1", "45.33.32.156", "91.240.118.172", "23.94.5.100"}
```

---

## Aula 8 — Tratamento de Exceções

Tratamento de exceções é o mecanismo que permite ao programa lidar com erros durante a execução sem que ele simplesmente trave e feche. Quando algo inesperado acontece — o usuário digita uma letra onde deveria ser número, um arquivo não existe, a conexão de rede cai — Python gera uma exceção. Se essa exceção não for tratada, o programa para imediatamente e exibe uma mensagem de erro.
Na prática, erros vão acontecer. Um programa robusto não é aquele que nunca encontra erros, mas aquele que sabe reagir quando eles aparecem. Imagine um scanner de portas que testa 1000 portas de um servidor: se a conexão falha na porta 47 e o programa trava, você perde as outras 953 verificações. Com tratamento de exceções, o programa registra a falha e continua.
O conceito funciona como um plano B: você diz ao Python "tente executar este código, mas se der um erro específico, faça isso em vez de travar". É a diferença entre um programa amador que mostra Traceback (most recent call last)... para o usuário e um programa profissional que exibe "Senha inválida, tente novamente".


### 8.1 Tipos Comuns

| Exceção | Quando Ocorre |
|---------|---------------|
| `ValueError` | Valor inadequado (`int("abc")`) |
| `TypeError` | Tipo inadequado (`"2" + 2`) |
| `ZeroDivisionError` | Divisão por zero |
| `FileNotFoundError` | Arquivo não encontrado |
| `IndexError` | Índice fora do alcance |
| `KeyError` | Chave inexistente no dicionário |
| `ConnectionError` | Falha na conexão |

### 8.2 try / except

```python
try:
    numero = int(input("Digite um número: "))
    resultado = 100 / numero
    print(f"Resultado: {resultado}")
except ValueError:
    print("Erro: Digite apenas números!")
except ZeroDivisionError:
    print("Erro: Não é possível dividir por zero!")
```

### 8.3 try / except / else / finally

```python
try:
    arquivo = open("dados.txt", "r")
    conteudo = arquivo.read()
except FileNotFoundError:
    print("Arquivo não encontrado!")
else:
    print(f"Conteúdo: {conteudo}")   # Se NÃO houve exceção
finally:
    print("Operação finalizada.")    # SEMPRE executado
```

### 8.4 Levantando Exceções

```python
def verificar_idade(idade):
    if idade < 0:
        raise ValueError("Idade não pode ser negativa!")
    return True

try:
    verificar_idade(-5)
except ValueError as e:
    print(f"Erro: {e}")
```

## Exercício: 
1) Leitura Segura: Crie um programa que peça ao usuário 5 números e calcule a média. 
O programa não deve aceitar entradas inválidas (letras, caracteres especiais, valores vazios) 
— quando o usuário errar, exiba uma mensagem e peça novamente, sem contar como tentativa válida. 
Dados para testar: tente digitar abc, 12.5, "" (vazio), 100, @#$.

2) — Divisão Segura: Crie uma calculadora de divisão que receba dois números e trate: divisão por zero, 
entrada não numérica e números negativos (exiba um aviso mas permita). Ao final, 
mostre o resultado com 2 casas decimais. Teste com estas entradas:

```python 
testes = [
    ("10", "3"),      # Divisão normal
    ("10", "0"),      # Divisão por zero
    ("abc", "5"),     # Entrada inválida
    ("7", "xyz"),     # Entrada inválida
    ("-15", "4"),     # Número negativo (aviso)
    ("", "5"),        # Entrada vazia
]
```

3) Login com Tentativas: Crie um sistema de login que permita no máximo 3 tentativas. 
O programa deve tratar entradas vazias (usuário ou senha em branco), 
diferenciar entre usuário inexistente e senha incorreta, e bloquear o acesso após 3 falhas mostrando quanto tempo aguardar. 
Use esta base de usuários:

```python 
usuarios = {
    "admin": "Cyber@2024",
    "analista": "S3gur4nca!",
    "estagiario": "Mudar@123"
}
```


---

## Aula 9 — Check Point 02

### Revisão (Aulas 6-8)

- **Laços:** for, while, range(), break, continue
- **Estruturas de dados:** Listas, tuplas, dicionários
- **Exceções:** try/except/else/finally, raise

> **Exercício 1 — Analisador de Logs:** 
> **Exercício 2 — Cifra de César:**

---

## Aula 10 — Funções

Uma **função** é um bloco de código reutilizável que recebe dados de entrada (parâmetros), executa uma tarefa e pode devolver um resultado (retorno). Funções existem para resolver um problema central da programação: **evitar repetição**. Se você precisa verificar a força de uma senha em 10 lugares diferentes do seu programa, não faz sentido copiar o mesmo código 10 vezes — você escreve uma função uma vez e chama onde precisar.

Além de evitar repetição, funções tornam o código mais legível e organizado. Compare:

```python
# Sem funções — código difícil de entender
h = hashlib.sha256("senha".encode()).hexdigest()
p = 0
if len("senha") >= 8: p += 1
if any(c.isupper() for c in "senha"): p += 1
# ... mais 20 linhas misturadas

# Com funções — código auto-explicativo
h = gerar_hash("senha")
forca = verificar_senha("senha")
```

No segundo exemplo, mesmo sem ver o código interno das funções, você entende o que está acontecendo. O nome da função funciona como documentação.

### 10.1 Definindo Funções

A estrutura básica de uma função em Python usa a palavra-chave `def`, seguida do nome, parênteses com os parâmetros e dois pontos. O corpo da função é indentado:

```python
def saudacao(nome):
    """Exibe uma saudação personalizada."""
    print(f"Olá, {nome}! Bem-vindo ao sistema.")

saudacao("Maria")    # Olá, Maria! Bem-vindo ao sistema.
saudacao("Carlos")   # Olá, Carlos! Bem-vindo ao sistema.
```

O texto entre `"""aspas triplas"""` logo após a definição é chamado de **docstring** — é a documentação da função. Não é obrigatório, mas é uma boa prática que ajuda outros desenvolvedores (e você no futuro) a entender o que a função faz.

#### Funções sem parâmetros e sem retorno

```python
def exibir_menu():
    print("=== Sistema de Segurança ===")
    print("[1] Escanear portas")
    print("[2] Verificar senha")
    print("[3] Gerar hash")
    print("[4] Sair")

exibir_menu()  # Apenas exibe, não recebe nada e não retorna nada
```

### 10.2 Parâmetros e Retorno

Parâmetros são os dados que a função recebe para trabalhar. O `return` devolve um resultado para quem chamou a função. Quando uma função não tem `return`, ela retorna `None` automaticamente.

```python
def calcular_area(base, altura):
    return base * altura

area = calcular_area(5, 3)  # area recebe 15
print(area)

# A diferença entre print e return:
# print() apenas exibe na tela — o valor se perde
# return devolve o valor — você pode guardá-lo em uma variável
```

#### Parâmetros com valor padrão

Você pode definir valores padrão para parâmetros. Se o chamador não passar aquele argumento, o valor padrão é usado:

```python
def conectar(host, porta=80, protocolo="http"):
    print(f"Conectando a {protocolo}://{host}:{porta}")

conectar("exemplo.com")                    # usa porta=80, protocolo="http"
conectar("exemplo.com", 443, "https")      # sobrescreve os padrões
conectar("exemplo.com", protocolo="https") # pula porta, muda protocolo
```

#### Retornando múltiplos valores

Python permite retornar múltiplos valores de uma vez — internamente, eles são empacotados em uma tupla:

```python
def analisar_ip(ip):
    partes = ip.split(".")
    eh_valido = len(partes) == 4 and all(0 <= int(p) <= 255 for p in partes)
    eh_privado = ip.startswith("192.168.") or ip.startswith("10.")
    return eh_valido, eh_privado

valido, privado = analisar_ip("192.168.1.1")
print(f"Válido: {valido}, Privado: {privado}")
# Válido: True, Privado: True
```

### 10.3 Escopo de Variáveis

Variáveis criadas **dentro** de uma função só existem dentro dela — isso se chama **escopo local**. Variáveis criadas fora das funções têm **escopo global** e podem ser lidas (mas não modificadas) de dentro:

```python
mensagem = "Olá"  # Variável global

def saudacao():
    nome = "Carlos"             # Variável local — só existe aqui dentro
    print(f"{mensagem}, {nome}")

saudacao()       # "Olá, Carlos"
print(mensagem)  # "Olá" — funciona, é global
print(nome)      # ERRO! nome não existe fora da função
```

Na prática, evite variáveis globais quando possível. Passe os dados que a função precisa como parâmetros e receba os resultados via `return` — isso torna o código mais previsível e fácil de debugar.

### 10.4 *args e **kwargs

Às vezes você não sabe de antemão quantos argumentos a função vai receber. O `*args` aceita qualquer quantidade de argumentos posicionais (armazena como tupla) e o `**kwargs` aceita argumentos nomeados (armazena como dicionário):

```python
# *args — quantidade variável de argumentos posicionais
def somar(*numeros):
    return sum(numeros)

print(somar(1, 2, 3))         # 6
print(somar(10, 20, 30, 40))  # 100

# **kwargs — quantidade variável de argumentos nomeados
def criar_perfil(**dados):
    for chave, valor in dados.items():
        print(f"{chave}: {valor}")

criar_perfil(nome="Ana", cargo="Analista", setor="SOC")
# nome: Ana
# cargo: Analista
# setor: SOC
```

Um uso prático em segurança — função que aceita qualquer filtro:

```python
def buscar_logs(**filtros):
    """Busca logs aplicando filtros dinâmicos."""
    print("Buscando logs com filtros:")
    for campo, valor in filtros.items():
        print(f"  {campo} = {valor}")

buscar_logs(nivel="ERROR", ip="185.220.101.1")
buscar_logs(nivel="WARNING", usuario="admin", data="2025-02-20")
```

### 10.5 Funções Lambda

Funções lambda são funções anônimas (sem nome) escritas em uma única linha. São úteis para operações curtas e simples, especialmente quando usadas como argumento de outra função:

```python
quadrado = lambda x: x ** 2
print(quadrado(5))  # 25

# Equivalente a:
def quadrado(x):
    return x ** 2
```

O uso mais comum de lambda é em funções como `sort()`, `filter()` e `map()`:

```python
# Ordenar lista de dicionários por um campo
usuarios = [
    {"nome": "Ana", "nivel": 3},
    {"nome": "Bruno", "nivel": 1},
    {"nome": "Carlos", "nivel": 5}
]
usuarios.sort(key=lambda u: u["nivel"])
# Ordena por nível: Bruno(1), Ana(3), Carlos(5)

# Filtrar apenas níveis altos
admins = list(filter(lambda u: u["nivel"] >= 3, usuarios))
# [{"nome": "Ana", "nivel": 3}, {"nome": "Carlos", "nivel": 5}]
```

### 10.6 Funções como Objetos

Em Python, funções são objetos — podem ser armazenadas em variáveis, passadas como argumentos e colocadas em dicionários. Isso permite padrões poderosos:

```python
# Menu de operações usando dicionário de funções
def escanear():
    print("Escaneando portas...")

def verificar():
    print("Verificando senha...")

def gerar():
    print("Gerando hash...")

operacoes = {
    "1": escanear,    # Sem parênteses! Armazena a função, não o resultado
    "2": verificar,
    "3": gerar,
}

escolha = input("Opção: ")
if escolha in operacoes:
    operacoes[escolha]()  # Chama a função armazenada
else:
    print("Opção inválida")
```

### 10.7 Exemplo: Toolkit de Segurança

```python
import hashlib

def gerar_hash(texto, algoritmo="sha256"):
    """Gera hash criptográfico de um texto."""
    if algoritmo == "md5":
        return hashlib.md5(texto.encode()).hexdigest()
    elif algoritmo == "sha512":
        return hashlib.sha512(texto.encode()).hexdigest()
    return hashlib.sha256(texto.encode()).hexdigest()

def verificar_senha(senha):
    """Avalia a força de uma senha retornando o nível."""
    pontos = 0
    if len(senha) >= 8:
        pontos += 1
    if any(c.isupper() for c in senha):
        pontos += 1
    if any(c.islower() for c in senha):
        pontos += 1
    if any(c.isdigit() for c in senha):
        pontos += 1
    if any(c in "!@#$%&*" for c in senha):
        pontos += 1
    niveis = {0: "Muito fraca", 1: "Fraca", 2: "Razoável",
              3: "Boa", 4: "Forte", 5: "Muito forte"}
    return niveis.get(pontos, "Desconhecido")

def validar_ip(ip):
    """Verifica se um endereço IPv4 é válido."""
    partes = ip.split(".")
    if len(partes) != 4:
        return False
    for p in partes:
        try:
            if not 0 <= int(p) <= 255:
                return False
        except ValueError:
            return False
    return True

# Testando as funções
senha = "Cyb3r@Sec"
print(f"Força: {verificar_senha(senha)}")
print(f"SHA-256: {gerar_hash(senha)}")
print(f"MD5: {gerar_hash(senha, 'md5')}")
print(f"IP válido: {validar_ip('192.168.1.1')}")   # True
print(f"IP válido: {validar_ip('999.0.0.1')}")      # False
```

### 10.8 Boas Práticas

- **Cada função deve fazer UMA coisa** — se a descrição da função precisa da palavra "e", provavelmente deveria ser duas funções
- **Nomes descritivos** — `verificar_senha()` é melhor que `vs()` ou `func1()`
- **Docstrings** — documente o que a função faz, especialmente se outros vão usar
- **Evite funções longas** — se a função tem mais de 20-30 linhas, considere dividir
- **Retorne valores em vez de imprimir** — `return` torna a função reutilizável; `print` dentro da função limita o uso dela
- **Evite variáveis globais** — passe dados como parâmetros

## Exercício: 
1) Valide emails. 

Crie uma função que valide endereços de email verificando: se contém exatamente um @, se tem pelo menos um . depois do @, se não começa nem termina com @ ou ., e se não contém espaços. Teste com estas entradas:
```python
emails = [
    "carlos@empresa.com",       # Válido
    "ana.silva@fiap.com.br",    # Válido
    "invalido@",                # Inválido — nada depois do @
    "@empresa.com",             # Inválido — nada antes do @
    "sem.arroba.com",           # Inválido — falta @
    "dois@@email.com",          # Inválido — dois @
    "espaco errado@email.com",  # Inválido — contém espaço
    "admin@servidor",           # Inválido — sem . depois do @
    ".inicio@email.com",        # Inválido — começa com .
    "user@email.com.",          # Inválido — termina com .
]
``` 

2) Filtre IPs válidos. 

Crie uma função que receba uma lista de strings e retorne apenas os endereços IPv4 válidos (4 octetos de 0 a 255, separados por ponto). Separe o resultado em IPs privados (10.x.x.x, 172.16-31.x.x, 192.168.x.x) e públicos. Teste com:
```python
entradas = [
    "192.168.1.1",       # Válido — privado
    "8.8.8.8",           # Válido — público
    "256.1.1.1",         # Inválido — octeto > 255
    "10.0.0.5",          # Válido — privado
    "172.16.50.1",       # Válido — privado
    "abc.def.ghi.jkl",   # Inválido — não são números
    "192.168.1",         # Inválido — faltam octetos
    "1.2.3.4.5",         # Inválido — octetos demais
    "172.32.0.1",        # Válido — público (172.32 não é privado)
    "0.0.0.0",           # Válido — público
    "192.168.1.999",     # Inválido — octeto > 255
    "",                  # Inválido — vazio
]
```

3) Mini gerenciador de senhas.

Crie um programa que armazene senhas usando um dicionário (serviço como chave, senha como valor). O programa deve: adicionar novas senhas, buscar a senha de um serviço, gerar senhas aleatórias (use o módulo random com letras, números e símbolos), avaliar a força da senha ao cadastrar, e salvar/carregar os dados de um arquivo JSON. Use estes dados iniciais:

```python
senhas = {
    "gmail": "MinhaS3nha!",
    "github": "Dev@2024Seguro",
    "servidor_ssh": "R00t#Acesso",
    "banco_dados": "db123",
}

# Critérios de força:
# Fraca: menos de 8 caracteres
# Média: 8+ caracteres com letras e números
# Forte: 8+ caracteres com maiúsculas, minúsculas, números e símbolos
``` 
---

## Aula 11 — Módulos e Comandos do Sistema

Um módulo em Python é simplesmente um arquivo .py que contém código reutilizável — funções, variáveis, classes. 
Em vez de escrever tudo em um único arquivo gigante, você separa o código em módulos organizados por responsabilidade e importa apenas o que precisa.
Python já vem com uma vasta biblioteca padrão — uma coleção de módulos prontos que cobrem desde manipulação de arquivos até criptografia. 
Isso significa que, antes de sair programando uma solução do zero, vale verificar se Python já não resolve o problema para você. 
Alguns exemplos relevantes para segurança: os para interagir com o sistema operacional, subprocess para executar comandos externos, hashlib para gerar hashes criptográficos, socket para comunicação em rede.

Além da biblioteca padrão, existem módulos de terceiros criados pela comunidade, instaláveis via PIP — como requests, scapy, nmap. 
E você também pode criar seus próprios módulos: basta colocar suas funções em um arquivo .py separado e importá-lo em outro.

A ideia central é: escreva uma vez, use em qualquer lugar. Se você criou uma função que valida endereços IP, não faz sentido copiá-la em cada novo projeto. 
Coloque-a em um módulo seguranca.py e importe quando precisar.


### 11.1 Importando Módulos

```python
import os
print(os.getcwd())

from datetime import datetime
print(datetime.now())

import random as rd
print(rd.randint(1, 100))
```

### 11.2 Módulo os

O módulo os é a ponte entre o Python e o sistema operacional. Ele permite que seu programa interaja com o ambiente onde está rodando — navegar por diretórios, listar arquivos, ler variáveis de ambiente, obter informações sobre o sistema. É como ter acesso ao terminal de dentro do seu código Python.Em segurança, os é útil para automatizar tarefas de administração: verificar permissões de arquivos, percorrer diretórios em busca de arquivos suspeitos, ler variáveis de ambiente onde credenciais podem estar expostas.

```python
import os

# Informações do sistema
print(os.name)              # 'nt' (Windows) ou 'posix' (Linux/Mac)
print(os.getcwd())          # Diretório atual de trabalho

# Navegação e manipulação de diretórios
os.mkdir('relatorios')      # Cria um diretório
os.listdir('.')             # Lista arquivos e pastas do diretório atual
os.rename('antigo.txt', 'novo.txt')
os.remove('arquivo.txt')    # Deleta um arquivo

# Variáveis de ambiente — importante em segurança
# (credenciais nunca devem estar no código, e sim em variáveis de ambiente)
api_key = os.environ.get('API_KEY')

# Caminhos de forma segura (funciona em qualquer SO)
caminho = os.path.join('home', 'usuario', 'documentos', 'relatorio.pdf')
print(os.path.exists(caminho))   # True ou False
```

### 11.3 Módulo subprocess

O módulo subprocess permite executar comandos do sistema operacional de dentro do Python e capturar o resultado. 
É como se você abrisse o terminal, digitasse um comando e pudesse ler a saída programaticamente.

A diferença para o os é que os interage com o sistema através de funções Python, enquanto subprocess executa literalmente 
comandos externos — qualquer coisa que você digitaria no terminal. Isso dá muito poder, mas também muito risco: se a entrada do 
usuário for passada diretamente para um comando sem sanitização, você cria uma vulnerabilidade de Command Injection.

```python
import subprocess

# Executar um comando e capturar a saída
resultado = subprocess.run(
    ["ping", "-c", "4", "google.com"],
    capture_output=True,
    text=True
)
print(resultado.stdout)      # Saída do comando
print(resultado.returncode)  # 0 = sucesso

# Listar processos (Linux)
resultado = subprocess.run(
    ["ps", "aux"],
    capture_output=True,
    text=True
)
print(resultado.stdout)

# Verificar se um serviço está rodando
resultado = subprocess.run(
    ["systemctl", "status", "nginx"],
    capture_output=True,
    text=True
)
if resultado.returncode == 0:
    print("Nginx está ativo")
else:
    print("Nginx está parado")
```

> ⚠️ Nunca use subprocess com entrada do usuário sem sanitização! Risco de Command Injection.

```python 
# PERIGOSO — Command Injection
ip = input("Digite o IP: ")
# Se o usuário digitar: 8.8.8.8 ; rm -rf /
subprocess.run(f"ping -c 4 {ip}", shell=True)  # NUNCA faça isso!

# SEGURO — passando como lista (cada argumento separado)
subprocess.run(["ping", "-c", "4", ip])  # Correto
``` 

### 11.4 Módulo hashlib

O módulo hashlib gera hashes criptográficos — funções que transformam qualquer dado em uma sequência fixa de caracteres, 
de forma irreversível. O mesmo dado sempre gera o mesmo hash, mas é praticamente impossível descobrir o dado original a partir do hash.

Em segurança, hashes são usados em todo lugar: armazenar senhas (nunca guarde senhas em texto puro), 
verificar integridade de arquivos (um malware altera o hash), identificar malware em bases de dados de ameaças (cada malware tem um hash único), 
e criar assinaturas digitais.

```python
import hashlib

texto = "senha_secreta"

# MD5 — rápido, mas considerado inseguro para senhas
# Ainda útil para verificação de integridade de arquivos
md5 = hashlib.md5(texto.encode()).hexdigest()
print(f"MD5:     {md5}")
# d35739089d8523bff1e99a8e0a700717

# SHA-256 — seguro e amplamente utilizado
sha256 = hashlib.sha256(texto.encode()).hexdigest()
print(f"SHA-256: {sha256}")
# 2bb80d537b1da3e38bd30361aa855686bde0eacd7162fef6a25fe97bf527a25b

# SHA-512 — ainda mais seguro, hash mais longo
sha512 = hashlib.sha512(texto.encode()).hexdigest()
print(f"SHA-512: {sha512}")

# Verificar integridade de um arquivo
def hash_arquivo(caminho):
    sha256 = hashlib.sha256()
    with open(caminho, "rb") as f:
        while bloco := f.read(8192):
            sha256.update(bloco)
    return sha256.hexdigest()

# Se o hash mudou, o arquivo foi alterado
print(hash_arquivo("documento.pdf"))
```


Algoritmo | Tamanho do Hash | Segurança | Uso Comum | 
|---------|---------|---------|---------|
MD5 | 128 bits (32 caracteres) | Fraco — vulnerável a colisões | Checksum de arquivos | 
SHA-1 | 160 bits (40 caracteres) | Fraco — descontinuado | Legado (evitar) | 
SHA-256 | 256 bits (64 caracteres) | Forte | Senhas, integridade, blockchain | 
SHA-512 | 512 bits (128 caracteres) | Muito forte | Aplicações críticas | 


### 11.5 Criando Seus Próprios Módulos

```python
# arquivo: seguranca.py
def validar_ip(ip):
    partes = ip.split('.')
    if len(partes) != 4:
        return False
    for p in partes:
        try:
            if not 0 <= int(p) <= 255:
                return False
        except ValueError:
            return False
    return True

# arquivo: main.py
from seguranca import validar_ip
ip = input("IP: ")
print("Válido!" if validar_ip(ip) else "Inválido!")
```

## Exercício: 
1) Módulo de criptografia (MD5, SHA-256, base64). 

Crie um arquivo cripto.py que funcione como módulo reutilizável com funções para: gerar hash MD5 e SHA-256 de um texto, codificar e decodificar em base64, e verificar a integridade de um arquivo comparando seu hash com um hash esperado. Depois crie um main.py que importe o módulo e teste todas as funções. Dados para teste:

```python
textos = [
    "senha_secreta",
    "Coding for Security - FIAP",
    "admin@2024",
    "",                          # String vazia (deve funcionar)
]

# Hash esperado para verificação de integridade
arquivo_teste = "documento.txt"  # Crie este arquivo com qualquer conteúdo
hash_esperado = "cole_aqui_o_hash_gerado_na_primeira_execucao"
```

2) Liste arquivos .py com os. 

Listador de Arquivos: Crie um programa que receba um caminho de diretório e liste todos os arquivos .py encontrados, incluindo subpastas (busca recursiva). Para cada arquivo, exiba: nome, caminho completo, tamanho em KB e data de última modificação. Ao final, mostre o total de arquivos encontrados e o tamanho somado. Teste com:

```python
import os

# Crie esta estrutura de pastas para testar:
# projeto/
# ├── main.py
# ├── config.json          (deve ser ignorado)
# ├── utils/
# │   ├── seguranca.py
# │   └── rede.py
# ├── logs/
# │   └── evento.log       (deve ser ignorado)
# └── testes/
#     ├── test_seguranca.py
#     └── test_rede.py

diretorio = "projeto"
extensao = ".py"
```

3) Ping em lista de hosts.

Crie um programa que receba uma lista de hosts, execute ping em cada um usando subprocess e gere um relatório com status (online/offline) e tempo de resposta. Trate timeouts e hosts inválidos com exceções. Dados para teste:

```python
hosts = [
    {"nome": "Google DNS",       "ip": "8.8.8.8"},
    {"nome": "Cloudflare DNS",   "ip": "1.1.1.1"},
    {"nome": "Gateway Local",    "ip": "192.168.1.1"},
    {"nome": "Servidor Interno", "ip": "10.0.0.50"},       # Provavelmente offline
    {"nome": "IP Inválido",      "ip": "999.999.999.999"}, # Deve tratar o erro
    {"nome": "Localhost",        "ip": "127.0.0.1"},
]

# Saída esperada (exemplo):
# Google DNS       (8.8.8.8)         ONLINE   12ms
# Cloudflare DNS   (1.1.1.1)         ONLINE    8ms
# Gateway Local    (192.168.1.1)     ONLINE    1ms
# Servidor Interno (10.0.0.50)       OFFLINE   timeout
# IP Inválido      (999.999.999.999) ERRO      IP inválido
# Localhost        (127.0.0.1)       ONLINE    <1ms
```


---

## Aula 12 — Escrita e Leitura de Arquivos

### 12.1 Modos de Abertura

| Modo | Descrição |
|------|-----------|
| `'r'` | Leitura (padrão) |
| `'w'` | Escrita (sobrescreve) |
| `'a'` | Append (adiciona ao final) |
| `'r+'` | Leitura e escrita |
| `'rb'` | Leitura binária |

### 12.2 Lendo Arquivos

```python
with open("dados.txt", "r") as arquivo:
    conteudo = arquivo.read()
    print(conteudo)

# Linha por linha
with open("dados.txt", "r") as arquivo:
    for linha in arquivo:
        print(linha.strip())
```

### 12.3 Escrevendo Arquivos

```python
with open("saida.txt", "w") as arquivo:
    arquivo.write("Primeira linha\n")
    arquivo.write("Segunda linha\n")

# Append
with open("log.txt", "a") as arquivo:
    arquivo.write("Nova entrada de log\n")
```

### 12.4 Exemplo: Analisador de Logs

```python
from datetime import datetime

def registrar_log(mensagem, nivel="INFO"):
    ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("security.log", "a") as log:
        log.write(f"[{ts}] [{nivel}] {mensagem}\n")

def analisar_logs(arquivo_log):
    contadores = {"INFO": 0, "WARNING": 0, "ERROR": 0}
    with open(arquivo_log, "r") as f:
        for linha in f:
            for nivel in contadores:
                if f"[{nivel}]" in linha:
                    contadores[nivel] += 1
    for nivel, count in contadores.items():
        print(f"{nivel}: {count} ocorrências")
```

## Exercício: 
1) Leia CSV e exiba formatado. 

Crie um programa que leia um arquivo CSV de inventário de ativos e exiba os dados formatados como tabela no terminal, com colunas alinhadas. Calcule e exiba ao final: total de ativos, quantos estão ativos/inativos e quantos são de cada tipo. Crie o arquivo ativos.csv para teste:

```
nome,tipo,ip,status,ultimo_acesso
SRV-WEB01,servidor,192.168.1.10,ativo,2025-02-20
SRV-DB01,servidor,192.168.1.20,ativo,2025-02-19
PC-RH03,estacao,192.168.1.45,inativo,2025-01-05
SW-CORE01,switch,192.168.1.1,ativo,2025-02-20
PC-MKT07,estacao,192.168.1.52,inativo,2024-11-30
RT-BORDA01,roteador,192.168.1.254,ativo,2025-02-18
SRV-MAIL01,servidor,192.168.1.30,inativo,2024-12-10
PC-DEV02,estacao,192.168.1.60,ativo,2025-02-20
```

2) Registro de usuários em arquivo. 

Crie um sistema que cadastre usuários em um arquivo texto, onde cada linha armazena: nome, email, nível de acesso e data de cadastro. O programa deve permitir cadastrar, listar e buscar por nome ou nível. Trate duplicatas de email e valide o nível de acesso (1 a 5). Crie o arquivo usuarios.txt com estes dados iniciais:

```
Carlos Silva|carlos@empresa.com|3|2025-01-15
Ana Costa|ana@empresa.com|5|2025-01-20
Bruno Lima|bruno@empresa.com|1|2025-02-01
Diana Souza|diana@empresa.com|4|2025-02-10
Eduardo Reis|eduardo@empresa.com|2|2025-02-15
```

3) IPs com muitas tentativas de login.

 Crie um programa que analise um arquivo de log de autenticação, identifique IPs com muitas tentativas de login falhas e gere um relatório de ameaças. Classifique: crítico (mais de 20 falhas), alto (mais de 10), médio (mais de 5). 
 
 Crie o arquivo auth.log com os dados de teste:

```log
2025-02-20 08:15:01 FAIL usuario=admin ip=185.220.101.1
2025-02-20 08:15:02 FAIL usuario=root ip=185.220.101.1
2025-02-20 08:15:03 OK usuario=carlos ip=192.168.1.10
2025-02-20 08:15:05 FAIL usuario=admin ip=91.240.118.172
2025-02-20 08:15:06 FAIL usuario=test ip=185.220.101.1
2025-02-20 08:15:08 FAIL usuario=admin ip=185.220.101.1
2025-02-20 08:15:10 OK usuario=ana ip=192.168.1.45
2025-02-20 08:15:12 FAIL usuario=root ip=91.240.118.172
2025-02-20 08:15:15 FAIL usuario=admin ip=45.33.32.156
2025-02-20 08:15:16 FAIL usuario=admin ip=185.220.101.1
2025-02-20 08:15:18 FAIL usuario=root ip=185.220.101.1
2025-02-20 08:15:20 FAIL usuario=guest ip=91.240.118.172
2025-02-20 08:15:22 FAIL usuario=admin ip=185.220.101.1
2025-02-20 08:15:25 OK usuario=bruno ip=10.0.0.5
2025-02-20 08:15:28 FAIL usuario=sa ip=185.220.101.1
2025-02-20 08:15:30 FAIL usuario=admin ip=91.240.118.172
2025-02-20 08:15:33 FAIL usuario=root ip=185.220.101.1
2025-02-20 08:15:35 FAIL usuario=test ip=45.33.32.156
2025-02-20 08:15:38 FAIL usuario=admin ip=185.220.101.1
2025-02-20 08:15:40 FAIL usuario=root ip=185.220.101.1
2025-02-20 08:15:42 OK usuario=diana ip=192.168.1.20
2025-02-20 08:15:45 FAIL usuario=admin ip=91.240.118.172
2025-02-20 08:15:48 FAIL usuario=oracle ip=45.33.32.156
```
---

## Aula 13 — Sockets

Um socket é um ponto de conexão que permite que dois programas se comuniquem através de uma rede. É o mecanismo fundamental por trás de praticamente tudo que acontece na internet — quando você acessa um site, envia um email ou faz uma chamada de vídeo, por baixo dos panos existem sockets conectando os dois lados.
A analogia mais simples é um telefonema: para que duas pessoas conversem, cada uma precisa de um aparelho (socket), um número de telefone (endereço IP) e uma linha disponível (porta). Uma pessoa liga (cliente) e a outra atende (servidor). Depois que a conexão é estabelecida, ambas podem enviar e receber dados.
Na prática, um socket é definido por três informações: o protocolo (TCP ou UDP), o endereço IP (quem) e a porta (qual serviço). Por exemplo, quando seu navegador acessa google.com, ele cria um socket TCP, conecta ao IP do Google na porta 443 (HTTPS), envia a requisição e recebe a página de volta.
Existem dois tipos principais de socket:

* TCP (Transmission Control Protocol): Garante que os dados cheguem completos, na ordem correta e sem erros. É como enviar uma carta registrada — mais lento, mas confiável. Usado em: navegação web, email, transferência de arquivos, SSH.
* UDP (User Datagram Protocol): Envia os dados sem garantia de entrega nem ordem. É como gritar uma mensagem — rápido, mas pode se perder. Usado em: jogos online, streaming de vídeo, DNS.

Para segurança, entender sockets é essencial. Um scanner de portas funciona criando sockets e tentando conectar em cada porta do alvo — se a conexão for aceita, a porta está aberta. Ferramentas como Nmap, Netcat e Wireshark operam diretamente sobre sockets. Ataques como port scanning, banner grabbing e man-in-the-middle exploram o funcionamento dos sockets.

### 13.1 Socket TCP — Cliente

```python
import socket
cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cliente.connect(("exemplo.com", 80))
requisicao = "GET / HTTP/1.1\r\nHost: exemplo.com\r\n\r\n"
cliente.send(requisicao.encode())
resposta = cliente.recv(4096)
print(resposta.decode())
cliente.close()
```

### 13.2 Socket TCP — Servidor

```python
import socket
servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
servidor.bind(('0.0.0.0', 9999))
servidor.listen(5)
print("Aguardando conexões...")
while True:
    conexao, endereco = servidor.accept()
    print(f"Conexão de {endereco}")
    dados = conexao.recv(1024).decode()
    print(f"Recebido: {dados}")
    conexao.send("Recebido!".encode())
    conexao.close()
```

### 13.3 Scanner de Portas

```python
import socket

def scanner_portas(host, inicio=1, fim=1024):
    print(f"Escaneando {host} ({inicio}-{fim})")
    abertas = []
    for porta in range(inicio, fim + 1):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(0.5)
            if sock.connect_ex((host, porta)) == 0:
                try:
                    srv = socket.getservbyport(porta)
                except:
                    srv = "?"
                print(f"Porta {porta}: ABERTA ({srv})")
                abertas.append(porta)
            sock.close()
        except:
            pass
    print(f"Total abertas: {len(abertas)}")

scanner_portas("127.0.0.1", 1, 100)
```


### 13.3 O que é Threading?

Imagine um restaurante com um único garçom. Se ele atende uma mesa por vez do início ao fim — anota o pedido, vai à cozinha, espera ficar pronto, entrega o prato — as outras mesas ficam esperando. Com múltiplos garçons (threads), várias mesas são atendidas ao mesmo tempo.

Threading é exatamente isso: a capacidade de um programa executar múltiplas tarefas ao mesmo tempo. Cada thread é como um fluxo de execução independente dentro do mesmo programa, compartilhando a mesma memória.

Sem threading, um servidor de socket aceita um cliente e fica travado atendendo ele — todos os outros clientes ficam na fila. Com threading, cada nova conexão ganha seu próprio thread, e o servidor continua livre para aceitar novas conexões.

> ⚠️ Use scanners APENAS em redes autorizadas!

## Exercício: 
1) Transferência de Arquivos via TCP: Crie dois programas: um servidor que fica aguardando arquivos e um cliente que envia. O servidor deve salvar o arquivo recebido com o nome original. Trate arquivos grandes enviando em blocos (chunks) e exiba uma barra de progresso simples. Teste com estes cenários:

```python
# Dados para teste — crie estes arquivos antes:
#
# pequeno.txt  → escreva qualquer texto curto
# medio.csv    → copie os dados do exercício de CSV (ativos.csv)
# grande.bin   → gere com Python:
#   with open("grande.bin", "wb") as f:
#       f.write(b"X" * 1_000_000)  # 1 MB de dados

# Como testar (dois terminais):
# Terminal 1 — rode o servidor:
#   python servidor.py
#   > Aguardando conexão na porta 9000...
#
# Terminal 2 — rode o cliente:
#   python cliente.py pequeno.txt
#   > Enviando pequeno.txt (45 bytes)...
#   > Concluído!

# Configuração
HOST = "127.0.0.1"
PORTA = 9000
TAMANHO_BLOCO = 4096  # Envia 4KB por vez
``` 


2) Escaneie 100 portas comuns. 

Scanner de Portas: Crie um scanner que teste as 100 portas mais comuns de um host e identifique quais estão abertas, exibindo o nome do serviço quando possível. Teste primeiro no localhost e depois em servidores públicos que permitem scan. Dados para teste:


```python
# Portas mais comuns em segurança
PORTAS_COMUNS = [
    21, 22, 23, 25, 53, 80, 110, 111, 135, 139,
    143, 443, 445, 993, 995, 1723, 3306, 3389,
    5432, 5900, 8080, 8443, 8888,
]

# Alvos para teste:
alvos = [
    "127.0.0.1",      # Localhost — scan seguro
    "tcpbin.com",      # Servidor público de teste (porta 4242)
    "scanme.nmap.org", # Servidor do Nmap liberado para scan de teste
]

# Saída esperada (exemplo):
# === Escaneando scanme.nmap.org ===
# Porta 22   ABERTA  (ssh)
# Porta 80   ABERTA  (http)
# Porta 443  FECHADA
# ...
# Scan concluído: 2 portas abertas de 23 testadas (1.3s)
``` 

Dica: scanme.nmap.org é um servidor mantido pelo projeto Nmap especificamente para testes de port scanning — é o único servidor público onde você tem permissão explícita para escanear.


3) Chat cliente/servidor.

Chat Cliente/Servidor: Crie um chat em tempo real onde múltiplos clientes se conectam a um servidor central. O servidor deve repassar as mensagens de um cliente para todos os outros (broadcast). Cada cliente escolhe um apelido ao conectar. Teste abrindo 3 terminais:

3.1) Crie o arquivo de cliente.py com o seguinte codigo: 
```python 
import socket
import threading

HOST = '127.0.0.1'
PORTA = 9001


def receber_mensagens(cliente):
    """Thread que fica ouvindo mensagens do servidor."""
    while True:
        try:
            dados = cliente.recv(4096).decode()
            if not dados:
                print("\nServidor desconectou.")
                break

            # Servidor pedindo apelido
            if dados == "APELIDO:":
                apelido = input("Apelido: ").strip()
                if not apelido:
                    apelido = "Anônimo"
                cliente.send(apelido.encode())
                continue

            print(f"\r{dados}")
            print(">> ", end="", flush=True)

        except (ConnectionResetError, ConnectionAbortedError):
            print("\nConexão perdida com o servidor.")
            break
        except OSError:
            break

    cliente.close()


def _client_connection_factory():
    # Conectar ao servidor
    cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        cliente.connect((HOST, PORTA))
    except ConnectionRefusedError:
        print(f"Erro: Não foi possível conectar a {HOST}:{PORTA}")
        print("Verifique se o servidor está rodando.")
        exit()
    finally:
        print(f"Conectado a {HOST}:{PORTA}")
        print("Comandos: /online (ver quem está on), /hora, /sair\n")
        return cliente

def thread_to_get_messages_factory(cliente):
    thread = threading.Thread(target=receber_mensagens, args=(cliente,))
    thread.daemon = True
    thread.start()
    return thread

def main():
    cliente = _client_connection_factory()

    # Thread para receber mensagens
    thread_to_get_messages_factory(cliente)

    # Loop principal — enviar mensagens
    while True:
        try:
            mensagem = input(">> ")
            if not mensagem:
                continue

            cliente.send(mensagem.encode())

            if mensagem.lower() == "/sair":
                print("Desconectando...")
                break
        except (BrokenPipeError, ConnectionResetError):
            print("Conexão perdida.")
            break
        except (KeyboardInterrupt, EOFError):
            cliente.send("/sair".encode())
            print("\nDesconectando...")
            break

    cliente.close()
``` 

3.2) Implemente o codigo do servidor que segue: 
```python
import socket
import threading
from datetime import datetime

# Configuração
HOST = '0.0.0.0'
PORTA = 9001
MAX_CLIENTES = 10

clientes = {}  # {conexao: apelido}
lock = threading.Lock()


def broadcast(mensagem, origem=None):
    """Envia mensagem para todos os clientes, exceto a origem."""

    # implemente a funcao broadcast para enviar a mensagem para todos os clientes, exceto a origem, 
    # use o lock para evitar problemas de concorrencia, caso de erro ao enviar a mensagem para um cliente, 
    # remova o cliente usando a funcao remover_cliente


def remover_cliente(conexao):
    """Remove um cliente da lista e notifica os outros."""

    # implemente a funcao remover_cliente para remover o cliente da lista de clientes, use o lock para evitar problemas de concorrencia, 
    # crie uma mensagem de log com os dados de hora, apelido e endereco de IP com o formato: [HH:MM:SS] - Apelido - (IP) saiu do chat, 
    # e envie uma mensagem de notificação para os outros clientes com o formato: [HH:MM:SS] *** Apelido saiu do chat ***

def _get_apelido(conexao):
    """Solicita o apelido do cliente e retorna."""
    # implemente a funcao _get_apelido para solicitar o apelido do cliente, use o lock para evitar problemas de concorrencia,
    # caso o client nao envie um apelido valido, crie um apelido anonimo usando o ip do cliente e a porta

def tratar_cliente(conexao, endereco):
    """Gerencia a comunicação com um cliente individual."""
    # 1. Solicitar apelido
    # criar a funcao _get_apelido para:  
    # Pedir apelido e colocar o apelido no retornar (dica para pegar o dado que o client enviou, use conexao.recv(1024).decode().strip()),
    # tratar o erro da estruturam, feche a conecao caso de erro, a execucao de onde o _get_apelido for chamada, deve ser parada para que a thread seja finalizada

    # 2 - Registrar cliente
    # salve o apelido e a conexao em um dicionario global, use o lock para evitar problemas de concorrencia

    # 3 - Anunciar nova conexão
    # crie uma mensagem de log com os dados de hora, apelido e endereco de IP com o formato: [HH:MM:SS] - Apelido - (IP) entrou no chat

    # 4 - Notificar outros clientes, 
    # chame a funcao broadcast para enviar uma mensagem de notificação para os outros clientes com o formato: [HH:MM:SS] *** Apelido entrou no chat ***

    # 5 - Enviar mensagem de boas-vindas ao novo cliente
    # envie uma mensagem de boas-vindas para o cliente que acabou de se conectar, com o formato: Bem-vindo, Apelido! Online: lista de clientes online separados por virgula, 
    # a mensagem deve ser enviada para o cliente que se conectou e nao para os outros cliente 
    
    # 6 - Loop de principal de mensagens
    # implemente o loop principal de mensagens para receber mensagens do cliente, caso o cliente envie um comando especial, 
    # execute a ação correspondente, caso contrário, repasse a mensagem para os outros clientes usando a funcao broadcast,
    # os comandos especiais são:
    # /sair - o cliente sai do chat, remova o cliente usando a funcao remover_cliente e saia do loop para finalizar a thread
    # /online - o cliente solicita a lista de clientes online, envie uma mensagem para o cliente com o formato: Online (n): lista de clientes online separados por virgula
    # /hora - o cliente solicita a hora do servidor, envie uma mensagem para o cliente com o formato: Hora do servidor: HH:MM:SS    
    # Exemplo: if mensagem.lower() == "/sair":
                    # break
    
    # Essa funcao dever rodar constantemente para receber as messagens das conexoes 
    # A funcao deve pegar as mensagens com uso de comando ja documentado na apostila
    # Utilize a funcao strip() de str para remover os espacos em branco no inicio e no final da mensagem
    # Imprima a mensagem no console do servidor com o formato: [HH:MM:SS] Apelido: mensagem, use a funcao datetime.now().strftime("%H:%M:%S") para pegar a hora atual do servidor
    # Use a funcao broadcast para enviar a mensagem para os outros clientes, com o formato: [HH:MM:SS] Apelido: mensagem, use a funcao datetime.now().strftime("%H:%M:%S") para pegar a hora atual do servidor
    # Trate os erros que a funcao pode ter, imprima no console do servidor o erro e remova o cliente usando a funcao remover_cliente, caso de erro, saia do loop para finalizar a thread e remova o cliente usando a funcao remover_cliente


def main():
    # Iniciar servidor
    servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    servidor.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    servidor.bind((HOST, PORTA))
    servidor.listen(MAX_CLIENTES)

    print(f"=== Servidor de Chat ===")
    print(f"Rodando em {HOST}:{PORTA}")
    print(f"Máximo de clientes: {MAX_CLIENTES}")
    print(f"Aguardando conexões...\n")

    while True:
        try:
            conexao, endereco = servidor.accept()
            thread = threading.Thread(
                target=tratar_cliente,
                args=(conexao, endereco),
                daemon=True
            )
            thread.start()
        except KeyboardInterrupt:
            print("\nEncerrando servidor...")
            broadcast("*** Servidor encerrando ***")
            servidor.close()
            break

main()
``` 


---
## Aula 14 — Requests e JSON

### O que é uma API?

Uma API (Application Programming Interface) é um ponto de acesso que permite que programas se comuniquem entre si. Quando você usa o Instagram no celular, o aplicativo não tem todos os dados armazenados localmente — ele faz requisições para a API do Instagram, que responde com suas fotos, comentários e curtidas.
A analogia mais simples é um restaurante: você (cliente) não vai até a cozinha preparar sua comida. Você fala com o garçom (API) que leva seu pedido (requisição) à cozinha (servidor), e traz de volta o prato (resposta). Você não precisa saber como a cozinha funciona — só precisa saber como falar com o garçom.
Na web, a maioria das APIs segue o padrão REST (Representational State Transfer), que usa o protocolo HTTP para trocar dados — geralmente em formato JSON.

### O que é HTTP?
HTTP (HyperText Transfer Protocol) é o protocolo que define como cliente e servidor se comunicam na web. Toda vez que você acessa um site, seu navegador envia uma requisição HTTP e recebe uma resposta HTTP.
Uma requisição HTTP tem três partes:

Método (verbo): O que você quer fazer (GET, POST, PUT, DELETE)
URL: Onde está o recurso (https://api.exemplo.com/usuarios)
Headers/Body: Informações extras e dados enviados

#### Uma resposta HTTP tem:

Status code: Número indicando o resultado (200, 404, 500)
Headers: Metadados da resposta
Body: Os dados retornados (geralmente JSON)

#### Verbos HTTP
Cada verbo representa uma intenção diferente sobre o recurso:


| Verbo | Descrição | Exemplo | Analogia | 
|------|-----------|------|------|
| GET | Buscar dados | Listar todos os usuários | Ler um livro | 
| POST | Criar dados | Cadastrar novo usuário | Escrever página nova | 
| PUT | Atualizar (completo) | Substituir todos os dados do usuário | Reescrever página inteira | 
| PATCH | Atualizar (parcial) | Alterar só o email | Corrigir um parágrafo | 
| DELETE | Remover | Deletar um usuário | Arrancar página do livro


```python
import requests

# GET — buscar dados
r = requests.get("https://api.github.com/users/octocat")

# POST — enviar/criar dados
r = requests.post("https://httpbin.org/post", json={"nome": "Carlos"})

# PUT — substituir dados
r = requests.put("https://httpbin.org/put", json={"nome": "Carlos", "idade": 26})

# PATCH — atualizar parcialmente
r = requests.patch("https://httpbin.org/patch", json={"idade": 27})

# DELETE — remover dados
r = requests.delete("https://httpbin.org/delete")
```

#### Status Codes
O servidor responde com um código numérico que indica o resultado:

| Código | Significado | Quando acontece |
|------|-----------|------|
| 200 | OK | Tudo certo |
| 201 | Created | Recurso criado com sucesso (após POST) | 
| 204 | No Content | Sucesso, mas sem corpo na resposta (após DELETE) | 
| 400 | Bad Request | Requisição mal formada | 
| 401 | Unauthorized | Sem autenticação | 
| 403 | Forbidden | Autenticado, mas sem permissão | 
| 404 | Not Found | Recurso não existe | 
| 429 | Too Many Requests | Limite de requisições excedido | 
| 500 | Internal Server Error | Erro no servidor | 


```python 
r = requests.get("https://api.github.com/users/octocat")

if r.status_code == 200:
    print("Sucesso!")
    dados = r.json()
elif r.status_code == 404:
    print("Usuário não encontrado")
elif r.status_code == 401:
    print("Não autorizado — verifique sua API key")
else:
    print(f"Erro inesperado: {r.status_code}")
``` 

#### O que é JSON?
JSON (JavaScript Object Notation) é o formato padrão para troca de dados entre sistemas. Ele ganhou esse papel porque é legível por humanos e fácil de processar por máquinas. Quando uma API responde, quase sempre o corpo da resposta é JSON.
JSON e Python se parecem muito, mas não são a mesma coisa:


JSONPython"texto" (aspas duplas obrigatórias)"texto" ou 'texto'true / falseTrue / FalsenullNoneApenas dadosDados + lógica


```python 
import json

# Python → JSON (serialização)
dados_python = {
    "nome": "Carlos",
    "ativo": True,             # True vira true
    "nivel": None,             # None vira null
    "habilidades": ["Python", "Linux"]
}
texto_json = json.dumps(dados_python, indent=2)
print(texto_json)
# {
#   "nome": "Carlos",
#   "ativo": true,
#   "nivel": null,
#   "habilidades": ["Python", "Linux"]
# }

# JSON → Python (desserialização)
texto = '{"ip": "192.168.1.1", "porta": 80, "ativo": true}'
dados = json.loads(texto)
print(dados["ip"])       # 192.168.1.1
print(type(dados))       # <class 'dict'>
print(dados["ativo"])    # True (convertido automaticamente)

# Salvar em arquivo
with open("config.json", "w") as f:
    json.dump(dados_python, f, indent=2, ensure_ascii=False)

# Ler de arquivo
with open("config.json", "r") as f:
    config = json.load(f)
```


#### Headers e Autenticação
APIs reais exigem autenticação — você precisa provar quem é antes de acessar os dados. Os métodos mais comuns são API Key e Bearer Token, enviados nos headers da requisição:


```python

# API Key — chave enviada no header
headers = {"x-api-key": "sua_chave_aqui"}
r = requests.get("https://api.exemplo.com/dados", headers=headers)

# Bearer Token (JWT) — token de autenticação
headers = {"Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."}
r = requests.get("https://api.exemplo.com/perfil", headers=headers)

# Basic Auth — usuário e senha
r = requests.get(
    "https://api.exemplo.com/dados",
    auth=("usuario", "senha")
)
```

#### Query Parameters
Parâmetros na URL que filtram ou personalizam a requisição:

```python
# Em vez de montar a URL manualmente:
# https://api.exemplo.com/busca?q=python&limit=10&page=2

# Use o parâmetro params — mais limpo e seguro
r = requests.get(
    "https://api.exemplo.com/busca",
    params={"q": "python", "limit": 10, "page": 2}
)
print(r.url)
# https://api.exemplo.com/busca?q=python&limit=10&page=2
```

#### Tratamento de Erros em Requisições
Requisições HTTP podem falhar de várias formas — conexão caiu, servidor demorou, URL errada. A biblioteca requests tem exceções específicas para cada caso:

```python 
import requests

def requisicao_segura(url, timeout=10):
    try:
        r = requests.get(url, timeout=timeout)
        r.raise_for_status()  # Levanta exceção se status >= 400
        return r.json()

    except requests.exceptions.ConnectionError:
        print("Erro: Não foi possível conectar ao servidor")
    except requests.exceptions.Timeout:
        print(f"Erro: Servidor não respondeu em {timeout}s")
    except requests.exceptions.HTTPError as e:
        print(f"Erro HTTP: {e.response.status_code}")
    except requests.exceptions.JSONDecodeError:
        print("Erro: Resposta não é JSON válido")
    except requests.exceptions.RequestException as e:
        print(f"Erro inesperado: {e}")

    return None

dados = requisicao_segura("https://api.github.com/users/octocat")
if dados:
    print(f"Nome: {dados['name']}")
```


## Exercício: 

1) Consulta de IP: Crie um programa que receba uma lista de IPs e consulte informações de cada um usando a API gratuita do ipinfo.io (https://ipinfo.io/{ip}/json). Exiba: cidade, região, país, organização e se é VPN/proxy. Gere um relatório classificando os IPs como internos ou externos. Dados para teste:

```python 

```


2) Monitor de Websites: Crie um programa que monitore uma lista de websites, verificando periodicamente (a cada 30 segundos) se estão online. Registre status code, tempo de resposta e horário da verificação. Salve o histórico em um arquivo JSON e alerte quando um site ficar offline. Dados para teste:

```python 
sites = [
    {"nome": "Google",     "url": "https://www.google.com"},
    {"nome": "GitHub",     "url": "https://api.github.com"},
    {"nome": "HTTPBin",    "url": "https://httpbin.org/get"},
    {"nome": "Inexistente","url": "https://site-que-nao-existe-xyz.com"},
    {"nome": "Lento",      "url": "https://httpbin.org/delay/5"},
]

# Saída esperada (exemplo):
# [14:30:01] Google        200  120ms  ONLINE
# [14:30:01] GitHub        200   85ms  ONLINE
# [14:30:02] HTTPBin       200  200ms  ONLINE
# [14:30:05] Inexistente   ---    ---  OFFLINE (ConnectionError)
# [14:30:10] Lento         ---    ---  OFFLINE (Timeout: 3s)
```


3) Explorador de API Pública: Crie um programa com menu interativo que consuma a API pública do GitHub (https://api.github.com). O programa deve permitir: buscar informações de um usuário (/users/{username}), listar os repositórios públicos do usuário (/users/{username}/repos), buscar detalhes de um repositório (/repos/{owner}/{repo}), e salvar todos os resultados em um arquivo JSON. Trate erros de conexão, timeout e limite de requisições (status 403). Dados para teste:

```python 
# Endpoints da API do GitHub (não precisa de autenticação)
BASE_URL = "https://api.github.com"

usuarios_teste = ["octocat", "torvalds", "guido"]

# Saída esperada (exemplo):
# === Perfil: torvalds ===
# Nome: Linus Torvalds
# Bio: None
# Repos públicos: 7
# Seguidores: 223000
#
# === Repositórios ===
# 1. linux     ★ 180000  (C)
# 2. subsurface ★ 2200   (C++)
# ...
```