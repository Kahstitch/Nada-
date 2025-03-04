# exemplo_while.py
# Este código demonstra o funcionamento do laço de repetição "while" em Python.
# O laço while é utilizado para repetir um bloco de código enquanto uma condição for verdadeira.

# Inicializa a variável 'contador' com o valor 1.
contador = 1

# Inicia o laço while: enquanto 'contador' for menor ou igual a 5, o bloco de código será executado.
while contador <= 5:
    # Exibe o valor atual de 'contador' na tela.
    print("Contador:", contador)
    
    # Incrementa o valor de 'contador' em 1 para que o laço avance e não gere um loop infinito.
    contador += 1

# Exibe uma mensagem indicando que o laço foi finalizado.
print("Fim do laço while")
