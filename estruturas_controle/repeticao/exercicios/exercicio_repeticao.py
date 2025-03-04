# exercicio_repeticao.py
# Este exercício propõe o desafio de calcular a soma dos números de 1 até N.
# O valor N é informado pelo usuário.
# O código utiliza o laço de repetição "while" para iterar de 1 até N e calcular a soma.

# Solicita ao usuário que insira um número inteiro positivo e o converte para inteiro.
n = int(input("Digite um número inteiro positivo: "))

# Inicializa a variável 'soma' que irá armazenar o resultado da soma dos números.
soma = 0

# Inicializa a variável 'contador' com o valor 1 para iniciar a contagem.
contador = 1

# Utiliza o laço while para iterar de 1 até N.
while contador <= n:
    # Adiciona o valor atual de 'contador' à variável 'soma'.
    soma += contador
    
    # Incrementa o 'contador' em 1 para avançar a iteração.
    contador += 1

# Após o término do laço, exibe o resultado final da soma.
print("A soma dos números de 1 até", n, "é:", soma)
