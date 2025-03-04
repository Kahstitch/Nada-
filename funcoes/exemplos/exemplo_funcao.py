# ---------------------------
# Exemplo: Definição e Uso de Funções
# ---------------------------

# Definição de uma função simples que imprime uma mensagem de saudação
def saudacao():
    """
    Esta função não recebe nenhum parâmetro e apenas exibe uma mensagem na tela.
    """
    print("Olá! Bem-vindo ao mundo das funções em Python.")

# Chamada da função para que a mensagem seja exibida
saudacao()

# ---------------------------
# Exemplo com Parâmetros e Retorno
# ---------------------------

def soma(a, b):
    """
    Esta função recebe dois números como entrada, realiza a soma e retorna o resultado.
    
    Parâmetros:
    a (int ou float) - Primeiro número
    b (int ou float) - Segundo número
    
    Retorno:
    int ou float - O resultado da soma de 'a' e 'b'
    """
    return a + b  # Retorna a soma dos dois números

# Chamada da função com valores específicos
resultado = soma(5, 3)

# Exibição do resultado
print("A soma de 5 e 3 é:", resultado)

# ---------------------------
# Exemplo com Valor Padrão para Parâmetro
# ---------------------------

def cumprimentar(nome="Aluno"):
    """
    Esta função exibe uma mensagem personalizada de cumprimento.
    Se nenhum nome for fornecido, usa o padrão "Aluno".
    
    Parâmetro:
    nome (str) - O nome da pessoa a ser cumprimentada (padrão: "Aluno")
    
    Retorno:
    Nenhum
    """
    print(f"Olá, {nome}! Espero que esteja gostando de aprender Python.")

# Chamada da função com e sem parâmetro
cumprimentar("Wendell")
cumprimentar()  # Aqui, será usado o valor padrão "Aluno"
