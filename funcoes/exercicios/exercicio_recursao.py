# ---------------------------
# Exercício: Função Recursiva para Fatorial
# ---------------------------

def calcular_fatorial(n):
    """
    Esta função calcula o fatorial de um número usando recursão.

    Parâmetro:
    n (int) - Número inteiro não negativo para calcular o fatorial.

    Retorno:
    int - O fatorial do número fornecido.
    """
    # Caso base: Se n for 0 ou 1, retorna 1 (condição de parada)
    if n == 0 or n == 1:
        return 1
    else:
        # Chamada recursiva: n * fatorial(n-1)
        return n * calcular_fatorial(n - 1)

# ---------------------------
# Teste da função com entrada do usuário
# ---------------------------

# Solicita ao usuário um número inteiro positivo
numero = int(input("Digite um número inteiro para calcular o fatorial: "))

# Verifica se o número é válido
if numero < 0:
    print("O fatorial não é definido para números negativos.")
else:
    # Chama a função e exibe o resultado
    print(f"O fatorial de {numero} é {calcular_fatorial(numero)}")
