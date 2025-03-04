"""
EXERCÍCIO - TRABALHANDO COM LISTAS EM PYTHON
Desafio: Crie um programa que gerencie uma lista de compras.
O usuário poderá adicionar itens, remover itens e visualizar a lista.
"""

# Inicializando uma lista vazia para armazenar os itens da compra
lista_compras = []

# Exibindo um menu para o usuário interagir
while True:
    print("\n=== LISTA DE COMPRAS ===")
    print("1 - Adicionar item")
    print("2 - Remover item")
    print("3 - Mostrar lista")
    print("4 - Sair")

    # Solicitando a escolha do usuário
    opcao = input("Escolha uma opção: ")

    # Opção 1: Adicionar item à lista
    if opcao == "1":
        item = input("Digite o nome do item: ")
        lista_compras.append(item)  # Adicionando o item à lista
        print(f'"{item}" foi adicionado à lista.')

    # Opção 2: Remover um item da lista
    elif opcao == "2":
        item = input("Digite o nome do item a ser removido: ")
        if item in lista_compras:
            lista_compras.remove(item)  # Removendo o item da lista
            print(f'"{item}" foi removido da lista.')
        else:
            print("O item não está na lista.")

    # Opção 3: Exibir a lista de compras
    elif opcao == "3":
        if lista_compras:
            print("Sua lista de compras contém:")
            for i, item in enumerate(lista_compras, start=1):
                print(f"{i}. {item}")  # Exibindo a lista numerada
        else:
            print("A lista de compras está vazia.")

    # Opção 4: Sair do programa
    elif opcao == "4":
        print("Saindo do programa...")
        break  # Encerra o loop

    # Caso o usuário escolha uma opção inválida
    else:
        print("Opção inválida! Tente novamente.")
