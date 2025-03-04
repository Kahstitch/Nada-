# ------------------------------------------
# Exemplo: Funções Avançadas em Python
# ------------------------------------------

# 📌 1. FUNÇÃO DENTRO DE FUNÇÃO (Nested Function)
# Uma função pode ser definida dentro de outra para encapsular comportamentos.

def saudacao_personalizada(nome):
    """
    Esta função recebe um nome e retorna uma mensagem de saudação personalizada.
    
    Parâmetro:
    nome (str) - O nome da pessoa a ser cumprimentada.
    
    Retorno:
    str - Mensagem de saudação personalizada.
    """

    # Definição de uma função interna
    def mensagem():
        return f"Olá, {nome}! Seja bem-vindo ao mundo da programação!"

    # Chamando a função interna e retornando o resultado
    return mensagem()

# Testando a função
print(saudacao_personalizada("Wendell"))

# ------------------------------------------
# 📌 2. FUNÇÃO LAMBDA (Função Anônima)
# Lambda é uma função sem nome, útil para expressões curtas.

# Criando uma função lambda que multiplica um número por 2
multiplicar_por_dois = lambda x: x * 2

# Testando a função lambda
print("O dobro de 5 é:", multiplicar_por_dois(5))

# ------------------------------------------
# 📌 3. FUNÇÕES COM *args e **kwargs
# *args - Recebe múltiplos argumentos como uma tupla.
# **kwargs - Recebe múltiplos argumentos nomeados como um dicionário.

def soma_varios(*args):
    """
    Esta função recebe vários números e retorna a soma deles.

    Parâmetro:
    *args (int ou float) - Vários números a serem somados.

    Retorno:
    int ou float - A soma de todos os números fornecidos.
    """
    return sum(args)  # Soma todos os valores dentro de *args

# Testando a função com múltiplos valores
print("Soma de 2, 4, 6, 8:", soma_varios(2, 4, 6, 8))

def dados_pessoais(**kwargs):
    """
    Esta função recebe dados pessoais como argumentos nomeados e os imprime.
    
    Parâmetros:
    **kwargs (dict) - Argumentos nomeados (exemplo: nome, idade, cidade).

    Retorno:
    Nenhum (apenas exibe as informações).
    """
    for chave, valor in kwargs.items():
        print(f"{chave.capitalize()}: {valor}")

# Testando a função com múltiplos dados
dados_pessoais(nome="Wendell", idade=18, cidade="Guarulhos")
