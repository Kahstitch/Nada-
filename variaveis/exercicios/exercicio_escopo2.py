# ---------------------------------------------------------------------
# Arquivo: exercicio_escopo2.py
# Localização: variaveis/exercicios/
#
# Este exercício propõe um desafio para o aluno aprofundar o entendimento sobre 
# escopo de variáveis, incluindo o uso de funções aninhadas e a manipulação de variáveis
# globais e locais.
#
# Desafio:
# 1. Crie uma variável global chamada 'mensagem_principal' com o valor 
#    "Bem-vindo(a) ao mundo das variáveis!".
# 2. Defina uma função 'exibir_mensagem' que contenha:
#    - Uma função interna chamada 'mensagem_secundaria' que:
#         * Declare uma variável local 'nota' com o valor "Lembre-se de praticar sempre!".
#         * Retorne a variável 'nota'.
#    - Dentro da função 'exibir_mensagem', chame a função 'mensagem_secundaria' e armazene
#      o valor retornado.
#    - Imprima a variável global 'mensagem_principal' e a mensagem retornada pela função interna.
#
# Após realizar o exercício, confira a solução comentada abaixo.
# ---------------------------------------------------------------------

# Declaração da variável global 'mensagem_principal'
mensagem_principal = "Bem-vindo(a) ao mundo das variáveis!"  # Variável global, disponível para todo o módulo

def exibir_mensagem():
    """
    Função para demonstrar o uso de escopo global, local e funções aninhadas.
    """
    # Função interna que possui seu próprio escopo
    def mensagem_secundaria():
        # Declaração de uma variável local à função interna
        nota = "Lembre-se de praticar sempre!"  # Variável local dentro da função 'mensagem_secundaria'
        return nota  # Retorna a mensagem para ser utilizada na função externa

    # Chamada da função interna e armazenamento do valor retornado
    mensagem_local = mensagem_secundaria()

    # Exibição das mensagens
    print("Mensagem Global:", mensagem_principal)  # Utiliza a variável global definida fora da função
    print("Mensagem da Função Interna:", mensagem_local)  # Exibe a mensagem retornada pela função interna

# Chamada da função 'exibir_mensagem' para demonstrar o comportamento dos escopos
exibir_mensagem()

# Explicação:
# - A variável 'mensagem_principal' é definida fora de qualquer função, tornando-a global.
# - Dentro da função 'exibir_mensagem', definimos uma função aninhada 'mensagem_secundaria' 
#   que cria e retorna uma variável local 'nota'.
# - Ao chamar 'exibir_mensagem', a função interna é executada e sua mensagem é capturada e exibida
#   juntamente com a mensagem global.
# - Este exercício ilustra como funções aninhadas podem ser utilizadas para encapsular lógica e
#   manter o código organizado e modular.
