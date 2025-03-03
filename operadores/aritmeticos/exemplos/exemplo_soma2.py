# exemplo_soma2.py
# Este exemplo demonstra o uso do operador de adição (+) de forma iterativa,
# somando todos os elementos de uma lista.
# O código foi elaborado para ilustrar como utilizar laços de repetição junto com a operação de soma.

# Declaração de uma lista de números
numeros = [5, 10, 15, 20]  # Lista contendo números inteiros para soma

# Inicialização da variável que armazenará a soma total dos números
soma_total = 0  # Variável iniciada com zero para acumular a soma

# Laço de repetição: percorre cada elemento da lista 'numeros'
for numero in numeros:
    soma_total += numero  # Operador '+=' adiciona o valor de 'numero' à 'soma_total'
    # A cada iteração, o valor atual da lista é somado ao total acumulado

# Exibe o resultado final da soma no console
print("A soma total dos números é:", soma_total)

# Resumo:
# - A lista 'numeros' contém os valores a serem somados.
# - O laço 'for' percorre cada elemento e o operador '+=' atualiza 'soma_total'.
# - Por fim, o comando 'print' exibe o resultado da operação.
