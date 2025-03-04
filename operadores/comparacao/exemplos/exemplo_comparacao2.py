# -----------------------------------------------
# EXEMPLO DE USO DOS OPERADORES DE COMPARAÇÃO
# COM STRINGS E LISTAS
# -----------------------------------------------

# 🔹 Comparação de strings
nome1 = "Alice"
nome2 = "Bob"

print("Comparação de Strings:")
print("Os nomes são iguais?", nome1 == nome2)  # False
print("Os nomes são diferentes?", nome1 != nome2)  # True
print("O nome1 vem antes do nome2 no alfabeto?", nome1 < nome2)  # True (A < B)
print("O nome2 vem depois do nome1 no alfabeto?", nome2 > nome1)  # True (B > A)
print()

# 🔹 Comparação de listas
lista1 = [1, 2, 3]
lista2 = [1, 2, 4]

print("Comparação de Listas:")
print("As listas são iguais?", lista1 == lista2)  # False (último elemento é diferente)
print("A lista1 é menor que a lista2?", lista1 < lista2)  # True ([1,2,3] < [1,2,4])
print("A lista1 é maior que a lista2?", lista1 > lista2)  # False
print()

# 🔹 Uso prático: checar presença de elementos
numero = 5
numeros_permitidos = [2, 4, 6, 8, 10]

print("Verificação de presença em listas:")
print("O número 5 está na lista?", numero in numeros_permitidos)  # False
print("O número 2 está na lista?", 2 in numeros_permitidos)  # True
