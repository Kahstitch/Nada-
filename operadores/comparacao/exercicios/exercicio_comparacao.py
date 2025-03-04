# ------------------------------------------------
# EXERCÍCIO: OPERADORES DE COMPARAÇÃO EM CONDICIONAIS
# ------------------------------------------------

# DESAFIO:
# O usuário deve inserir duas idades e o programa verificará:
# - Quem é mais velho.
# - Se as idades são iguais.
# - Se uma delas está dentro da faixa etária de 18 a 25 anos.

# Entrada de dados (o usuário digita dois valores inteiros)
idade1 = int(input("Digite a primeira idade: "))
idade2 = int(input("Digite a segunda idade: "))

# Comparação das idades
if idade1 > idade2:
    print("A primeira pessoa é mais velha.")
elif idade1 < idade2:
    print("A segunda pessoa é mais velha.")
else:
    print("As duas pessoas têm a mesma idade.")

# Verifica se alguma idade está entre 18 e 25 anos
if 18 <= idade1 <= 25 or 18 <= idade2 <= 25:
    print("Pelo menos uma das idades está entre 18 e 25 anos.")

# Saída final do programa
print("Comparação concluída.")
