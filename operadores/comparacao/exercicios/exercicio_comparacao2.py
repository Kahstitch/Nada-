# ------------------------------------------------
# EXERCÍCIO: COMPARAÇÃO DE STRINGS EM PYTHON
# ------------------------------------------------

# 🔹 Entrada de dados
palavra1 = input("Digite a primeira palavra: ").strip().lower()
palavra2 = input("Digite a segunda palavra: ").strip().lower()

# 🔹 Comparações entre as palavras
print("\nResultados da Comparação:")
if palavra1 == palavra2:
    print("As palavras são IGUAIS.")
else:
    print("As palavras são DIFERENTES.")

# 🔹 Verifica a ordem alfabética
if palavra1 < palavra2:
    print(f"A palavra '{palavra1}' vem antes de '{palavra2}' no alfabeto.")
else:
    print(f"A palavra '{palavra2}' vem antes de '{palavra1}' no alfabeto.")

# 🔹 Verifica se uma palavra está contida na outra
if palavra1 in palavra2 or palavra2 in palavra1:
    print("Uma das palavras está contida dentro da outra.")

# 🔹 Mensagem final
print("\nComparação concluída!")
