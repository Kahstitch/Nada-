# exercicio_repeticao2.py
# Este exercício propõe o desafio de calcular o fatorial de um número fornecido pelo usuário.
# O fatorial de um número n (representado por n!) é o produto de todos os inteiros positivos de 1 até n.
# Exemplo: 5! = 5 x 4 x 3 x 2 x 1 = 120
#
# O exercício utiliza o laço de repetição "while" para iterar e multiplicar os valores
# de forma incremental, demonstrando como construir uma solução passo a passo.

# Solicita ao usuário que insira um número inteiro positivo.
# A função input() captura a entrada do usuário e int() converte essa entrada para um valor inteiro.
n = int(input("Digite um número inteiro positivo para calcular seu fatorial: "))

# Inicializa a variável 'fatorial' com 1.
# Essa variável armazenará o resultado final do fatorial, que é uma multiplicação acumulada.
fatorial = 1

# Inicializa o contador com 1, que será utilizado para percorrer os números de 1 até n.
contador = 1

# Início do laço while:
# Enquanto o valor de 'contador' for menor ou igual a n, o laço se repete.
while contador <= n:
    # Atualiza a variável 'fatorial' multiplicando o valor atual pelo contador.
    fatorial *= contador
    
    # Exibe o passo atual do cálculo, permitindo ao aluno visualizar a evolução do fatorial.
    print("Passo:", contador, "-> Fatorial:", fatorial)
    
    # Incrementa o contador em 1 para avançar para o próximo número.
    contador += 1

# Após o término do laço, exibe o resultado final do cálculo.
print("O fatorial de", n, "é:", fatorial)
