"""
EXERCÍCIO: VERIFICAR SE UM USUÁRIO PODE VOTAR

Crie um programa que solicita a idade do usuário e informa se ele pode votar ou não.

REGRAS:
- Se a idade for menor que 16, exibir: "Você ainda não pode votar."
- Se a idade for entre 16 e 17 ou maior que 70, exibir: "O voto é opcional."
- Se a idade for entre 18 e 70, exibir: "O voto é obrigatório."
"""

# Solicita ao usuário que insira sua idade
idade = int(input("Digite sua idade: "))

# Estrutura condicional para verificar a elegibilidade para votar
if idade < 16:
    print("Você ainda não pode votar.")  # Caso a idade seja menor que 16
elif 16 <= idade < 18 or idade > 70:
    print("O voto é opcional.")  # Caso a idade esteja entre 16-17 ou seja maior que 70
else:
    print("O voto é obrigatório.")  # Caso a idade esteja entre 18-70

"""
EXPLICAÇÃO DA LÓGICA:
1. O programa recebe a idade como entrada do usuário.
2. Se a idade for menor que 16, exibe a mensagem informando que ele não pode votar.
3. Se a idade estiver entre 16 e 17 ou for maior que 70, o voto é opcional.
4. Se a idade estiver entre 18 e 70, o voto é obrigatório.

EXEMPLO DE ENTRADAS E SAÍDAS:
Entrada: 15 -> Saída: "Você ainda não pode votar."
Entrada: 16 -> Saída: "O voto é opcional."
Entrada: 25 -> Saída: "O voto é obrigatório."
Entrada: 72 -> Saída: "O voto é opcional."
"""
