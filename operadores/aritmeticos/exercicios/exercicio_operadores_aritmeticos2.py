# exercicio_operadores_aritmeticos2.py
# Exercício: Cálculo de Total e Desconto
#
# Descrição:
# Crie um programa que solicite ao usuário o preço de três produtos e, em seguida,
# realize as seguintes operações:
# 1. Calcule a soma total dos três preços.
# 2. Calcule a média aritmética dos preços.
# 3. Aplique um desconto de 10% sobre o valor total.
#
# Cada etapa do programa é detalhadamente comentada para facilitar o aprendizado.

# Entrada de dados:
# Solicita o preço do primeiro produto e converte a entrada para float
preco1 = float(input("Digite o preço do primeiro produto: "))
# Solicita o preço do segundo produto e converte a entrada para float
preco2 = float(input("Digite o preço do segundo produto: "))
# Solicita o preço do terceiro produto e converte a entrada para float
preco3 = float(input("Digite o preço do terceiro produto: "))

# Operações aritméticas:
# 1. Soma: calcula a soma total dos três preços.
soma_total = preco1 + preco2 + preco3  # Soma dos três preços

# 2. Média: calcula a média aritmética dividindo a soma total pelo número de produtos.
media_precos = soma_total / 3  # Média dos preços

# 3. Desconto: calcula 10% do valor total e deduz esse valor da soma total.
desconto = soma_total * 0.10  # Calcula 10% de desconto
valor_com_desconto = soma_total - desconto  # Valor final após aplicar o desconto

# Saída de dados:
# Exibe os resultados de forma clara e organizada.
print("\nResultados:")
print("Soma Total dos Produtos: R$", soma_total)
print("Média dos Preços: R$", media_precos)
print("Desconto (10%): R$", desconto)
print("Valor com Desconto: R$", valor_com_desconto)

# Explicação adicional:
# - O operador '+' soma os valores de 'preco1', 'preco2' e 'preco3'.
# - A divisão por 3 obtém a média aritmética dos três preços.
# - Multiplicar a soma_total por 0.10 calcula o valor do desconto (10%).
# - A subtração final aplica o desconto ao valor total.
# - A conversão para float permite que sejam usados valores decimais, comuns em preços.
