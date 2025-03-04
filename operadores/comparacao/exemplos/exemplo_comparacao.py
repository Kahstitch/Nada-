# -----------------------------------------------
# EXEMPLO DE USO DOS OPERADORES DE COMPARAÇÃO
# -----------------------------------------------

# Declaração de duas variáveis para comparar
a = 10
b = 5

# Comparações entre as variáveis
print("a =", a, ", b =", b)  # Exibe os valores de a e b
print("a == b ?", a == b)  # Verifica se a é igual a b
print("a != b ?", a != b)  # Verifica se a é diferente de b
print("a > b ?", a > b)    # Verifica se a é maior que b
print("a < b ?", a < b)    # Verifica se a é menor que b
print("a >= b ?", a >= b)  # Verifica se a é maior ou igual a b
print("a <= b ?", a <= b)  # Verifica se a é menor ou igual a b

# Exemplo de uso prático com condicional
if a > b:
    print("A variável 'a' é maior que 'b'.")

# Se as variáveis forem iguais, exibe outra mensagem
elif a == b:
    print("As variáveis 'a' e 'b' são iguais.")

else:
    print("A variável 'b' é maior que 'a'.")
