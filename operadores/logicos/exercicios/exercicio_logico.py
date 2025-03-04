# Exercício de operadores lógicos

# Pergunta ao usuário se ele tem idade para votar e se possui título de eleitor
idade = int(input("Digite sua idade: "))
tem_titulo = input("Você tem título de eleitor? (s/n): ").strip().lower() == "s"

# O usuário pode votar se tiver 16 anos ou mais e possuir título de eleitor
pode_votar = idade >= 16 and tem_titulo

# Exibe o resultado
print("Você pode votar?", pode_votar)

# Explicação:
# - O operador `>=` verifica se a idade é maior ou igual a 16.
# - O operador `and` garante que a pessoa precisa atender a AMBAS as condições para poder votar.
# - O operador `==` converte a resposta do usuário em um booleano (`True` para 's' e `False` para 'n').
