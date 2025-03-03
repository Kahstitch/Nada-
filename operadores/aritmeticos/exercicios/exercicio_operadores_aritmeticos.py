# exercicio_operadores_aritmeticos.py
# Exercício: Operadores Aritméticos
#
# Descrição:
# Crie um programa que solicite ao usuário que informe dois números e, em seguida, 
# exiba o resultado das seguintes operações:
# 1. Soma
# 2. Subtração
# 3. Multiplicação
# 4. Divisão (com resultado em ponto flutuante)
# 5. Divisão inteira (apenas a parte inteira)
# 6. Módulo (resto da divisão)
#
# O programa deve ser bem comentado e demonstrar o funcionamento de cada operação.

# Importante: Ao realizar testes, digite números válidos (inteiros ou decimais)

# Entrada de dados:
# Solicita ao usuário que insira o primeiro número e converte a entrada para float.
numero1 = float(input("Digite o primeiro número: "))
# Solicita ao usuário que insira o segundo número e converte a entrada para float.
numero2 = float(input("Digite o segundo número: "))

# Operações aritméticas:
# 1. Soma: utiliza o operador '+' para somar os dois números.
soma = numero1 + numero2  # Soma de numero1 e numero2

# 2. Subtração: utiliza o operador '-' para subtrair o segundo número do primeiro.
subtracao = numero1 - numero2  # Diferença entre numero1 e numero2

# 3. Multiplicação: utiliza o operador '*' para multiplicar os dois números.
multiplicacao = numero1 * numero2  # Produto de numero1 e numero2

# 4. Divisão: utiliza o operador '/' para dividir o primeiro número pelo segundo.
#    Obs: Se o segundo número for zero, isso gerará um erro (divisão por zero).
divisao = numero1 / numero2  # Resultado da divisão em ponto flutuante

# 5. Divisão inteira: utiliza o operador '//' para obter apenas a parte inteira da divisão.
divisao_inteira = numero1 // numero2  # Resultado da divisão inteira

# 6. Módulo: utiliza o operador '%' para obter o resto da divisão entre os dois números.
modulo = numero1 % numero2  # Resto da divisão de numero1 por numero2

# Saída de dados:
# Exibe os resultados de cada operação no console.
print("\nResultados das operações:")
print("Soma:", soma)
print("Subtração:", subtracao)
print("Multiplicação:", multiplicacao)
print("Divisão:", divisao)
print("Divisão Inteira:", divisao_inteira)
print("Módulo:", modulo)

# Explicação do exercício:
# Este exercício tem como objetivo fixar o uso dos operadores aritméticos em Python.
# Cada operação é realizada utilizando o operador correspondente e o resultado é impresso.
# O aluno pode testar com diferentes números e observar como cada operação se comporta,
# especialmente quando se trata de divisões e módulos.
