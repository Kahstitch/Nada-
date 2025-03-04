"""
EXEMPLO - LISTAS EM PYTHON
Este código demonstra como criar, modificar e acessar elementos de uma lista em Python.
Listas são usadas para armazenar múltiplos itens em uma única variável.
"""

# Criando uma lista com diferentes tipos de dados
# As listas em Python podem armazenar qualquer tipo de dado: números, strings, booleanos, etc.
minha_lista = [10, "Python", 3.14, True]

# Exibindo a lista completa
print("Lista completa:", minha_lista)

# Acessando elementos da lista pelo índice
print("Primeiro elemento (índice 0):", minha_lista[0])  # Saída: 10
print("Último elemento (índice -1):", minha_lista[-1])  # Saída: True

# Modificando um elemento da lista
minha_lista[1] = "Programação"
print("Lista após modificação:", minha_lista)

# Adicionando um novo elemento ao final da lista
minha_lista.append("Novo Item")
print("Lista após adicionar um item:", minha_lista)

# Removendo um elemento específico da lista
minha_lista.remove(3.14)
print("Lista após remover um item:", minha_lista)

# Percorrendo a lista com um loop
print("Percorrendo a lista:")
for item in minha_lista:
    print("-", item)

# Obtendo o tamanho da lista
print("A lista tem", len(minha_lista), "elementos.")

# Criando uma lista aninhada (lista dentro de lista)
lista_aninhada = [[1, 2, 3], ["A", "B", "C"], [True, False]]
print("Lista aninhada:", lista_aninhada)

# Acessando um elemento dentro da lista aninhada
print("Elemento na posição [1][2]:", lista_aninhada[1][2])  # Saída: "C"
