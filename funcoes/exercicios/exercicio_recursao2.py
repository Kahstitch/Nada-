# ------------------------------------------
# Exercício: Cálculo Recursivo da Sequência de Fibonacci
# ------------------------------------------

def fibonacci(n):
    """
    Esta função calcula o termo 'n' da sequência de Fibonacci usando recursão.

    A sequência de Fibonacci segue a seguinte regra:
    - fib(0) = 0
    - fib(1) = 1
    - fib(n) = fib(n-1) + fib(n-2) para n ≥ 2

    Parâmetro:
    n (int) - A posição desejada na sequência de Fibonacci.

    Retorno:
    int - O valor do termo na posição 'n' da sequência.
    """
    
    # Caso base: Se n for 0 ou 1, retorna o próprio valor de n
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        # Caso recursivo: Chama a própria função para os dois valores anteriores
        return fibonacci(n-1) + fibonacci(n-2)

# ------------------------------------------
# Teste com entrada do usuário
# ------------------------------------------

# Solicita ao usuário um número inteiro positivo
termo = int(input("Digite um número inteiro para calcular Fibonacci: "))

# Verifica se o número é válido
if termo < 0:
    print("A sequência de Fibonacci não é definida para números negativos.")
else:
    # Calcula e exibe o resultado
    print(f"O termo {termo} da sequência de Fibonacci é: {fibonacci(termo)}")
