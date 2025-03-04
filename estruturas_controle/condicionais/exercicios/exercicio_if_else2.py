"""
EXERCÍCIO: VERIFICAÇÃO DE ANO BISSEXTO

Crie um programa que solicite ao usuário um ano e verifique se ele é bissexto.
Um ano é considerado bissexto se atender às condições:
    - É divisível por 4 e não é divisível por 100, OU
    - É divisível por 400

O programa deve exibir uma mensagem informando se o ano é ou não bissexto.

Desafios Adicionais:
    - Valide a entrada do usuário para garantir que seja um número inteiro positivo.
    - Utilize estruturas condicionais aninhadas para uma lógica mais detalhada.
"""

# Solicita ao usuário que insira um ano
ano_str = input("Digite um ano (ex: 2024): ")

# Validação da entrada: verifica se o que foi digitado é um número inteiro positivo
if not ano_str.isdigit():
    print("Entrada inválida! Por favor, insira apenas números inteiros positivos.")
else:
    # Converte a entrada para um número inteiro
    ano = int(ano_str)
    
    # Verifica se o ano é bissexto usando estruturas condicionais aninhadas
    if ano % 4 == 0:  # Verifica se o ano é divisível por 4
        # Se for divisível por 4, checa a condição especial dos anos centenários
        if ano % 100 == 0:
            # Se for divisível por 100, somente será bissexto se também for divisível por 400
            if ano % 400 == 0:
                print(f"O ano {ano} é bissexto.")
            else:
                print(f"O ano {ano} não é bissexto.")
        else:
            # Se não for divisível por 100, mas for divisível por 4, é bissexto
            print(f"O ano {ano} é bissexto.")
    else:
        # Se não for divisível por 4, não é bissexto
        print(f"O ano {ano} não é bissexto.")

"""
EXPLICAÇÃO DA LÓGICA:
1. O programa começa solicitando um ano ao usuário e valida se a entrada é um número inteiro positivo.
2. Se a entrada for válida, converte-a para inteiro.
3. A estrutura condicional aninhada verifica:
    - Se o ano é divisível por 4.
        - Se sim, verifica se é um ano centenário (divisível por 100).
            - Se for centenário, o ano só é bissexto se for divisível por 400.
            - Se não for centenário, o ano é bissexto.
    - Caso o ano não seja divisível por 4, ele não é bissexto.
4. Cada etapa é comentada para facilitar o entendimento, detalhando a razão por trás de cada verificação.

EXEMPLOS:
Entrada: 2020 -> Saída: "O ano 2020 é bissexto."
Entrada: 1900 -> Saída: "O ano 1900 não é bissexto." (pois é centenário, mas não é divisível por 400)
Entrada: 2000 -> Saída: "O ano 2000 é bissexto."
"""
