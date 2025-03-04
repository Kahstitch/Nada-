"""
EXEMPLO DE CONDICIONAL IF-ELSE EM PYTHON

Este código verifica se um número digitado pelo usuário é positivo, negativo ou zero.
A estrutura `if-else` é utilizada para tomar a decisão com base no valor fornecido.
"""

# Solicita ao usuário que insira um número
numero = int(input("Digite um número inteiro: "))

# Estrutura condicional para verificar se o número é positivo, negativo ou zero
if numero > 0:
    print("O número é positivo.")  # Executado se a condição `numero > 0` for verdadeira
elif numero < 0:
    print("O número é negativo.")  # Executado se a condição `numero < 0` for verdadeira
else:
    print("O número é zero.")  # Executado se nenhuma das condições anteriores for atendida

"""
EXPLICAÇÃO:
1. O programa recebe um número inteiro do usuário.
2. Se o número for maior que zero, imprime "O número é positivo."
3. Se o número for menor que zero, imprime "O número é negativo."
4. Se nenhuma das condições for verdadeira, imprime "O número é zero."
"""
