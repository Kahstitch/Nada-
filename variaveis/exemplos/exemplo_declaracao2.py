# ---------------------------------------------------------------------
# Arquivo: exemplo_declaracao2.py
# Localização: variaveis/exemplos/
#
# Este exemplo demonstra uma variedade maior de declarações de variáveis
# em Python, incluindo conversões de tipos, operações aritméticas, concatenação
# de strings e a utilização de funções para formatar e exibir os dados.
#
# O código a seguir apresenta:
# - Declaração de variáveis com diferentes tipos de dados.
# - Conversão entre tipos (casting).
# - Operações matemáticas e aritméticas.
# - Concatenação e formatação de strings.
# - Impressão dos resultados na tela com explicações detalhadas.
# ---------------------------------------------------------------------

# Declaração de variáveis de diferentes tipos

# Variável inteira: armazena um número sem parte decimal.
idade = 25  # Exemplo: idade de uma pessoa

# Variável float: armazena um número com parte decimal.
altura = 1.75  # Exemplo: altura em metros

# Variável string: armazena uma sequência de caracteres.
nome = "Alice"  # Exemplo: nome da pessoa

# Variável booleana: armazena um valor True ou False.
maior_de_idade = True  # Indica se a pessoa é maior de idade

# Conversão de tipos (casting)
# Convertendo a idade para float para realizar uma divisão com precisão
idade_como_float = float(idade)  # Converte o inteiro 25 para 25.0

# Operação aritmética: cálculo do IMC (Índice de Massa Corporal)
# Fórmula: IMC = peso (kg) / (altura (m))²
peso = 68  # Peso em quilogramas
imc = peso / (altura ** 2)  # Calcula o IMC utilizando exponenciação para elevar a altura ao quadrado

# Concatenação e formatação de strings
# Utilizando f-string para incluir variáveis dentro da mensagem
mensagem_completa = f"Olá, {nome}! Você tem {idade} anos e sua altura é {altura}m."
mensagem_imc = f"Seu IMC calculado é: {imc:.2f}"  # :.2f formata o IMC com duas casas decimais

# Exibição dos resultados na tela com mensagens detalhadas
print("=== Demonstração Avançada de Variáveis ===")
print(mensagem_completa)     # Exibe a mensagem personalizada
print(mensagem_imc)          # Exibe o resultado do IMC
print("Idade convertida para float:", idade_como_float)  # Mostra o resultado da conversão
print("Status de maioridade:", maior_de_idade)  # Exibe se a pessoa é maior de idade

# Explicação:
# 1. Foram declaradas variáveis com diferentes tipos de dados, demonstrando a versatilidade
#    do Python na manipulação de informações.
# 2. A conversão de tipos (casting) é importante para operações que exigem precisão, como divisões.
# 3. O cálculo do IMC é um exemplo prático de como utilizar variáveis em operações matemáticas.
# 4. As f-strings facilitam a criação de mensagens dinâmicas e claras, integrando variáveis diretamente
#    na string.
