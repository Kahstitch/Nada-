"""
EXEMPLO AVANÇADO DE CONDICIONAIS: CLASSIFICAÇÃO DE DESEMPENHO ESTUDANTIL

Este exemplo demonstra o uso de condicionais aninhadas e operadores lógicos para
classificar o desempenho de um estudante com base na nota e na frequência (presença).

O programa solicita:
- A nota do estudante (de 0 a 100)
- A frequência (percentual de presença)

A partir destes dados, o programa classifica o desempenho em:
    - "Aprovado com Honras": Nota ≥ 90 e frequência ≥ 90%
    - "Aprovado": Nota ≥ 70 e frequência ≥ 75%
    - "Recuperação": Nota entre 50 e 69 ou frequência entre 50% e 74%
    - "Reprovado": Caso contrário

Cada etapa do código é comentada para facilitar a compreensão.
"""

# Solicita a nota do estudante (valor numérico entre 0 e 100)
nota = float(input("Digite a nota do estudante (0 a 100): "))

# Solicita a frequência (percentual de presença) do estudante
frequencia = float(input("Digite a frequência do estudante (0 a 100%): "))

# Verifica se os dados de entrada estão dentro dos intervalos esperados
if nota < 0 or nota > 100 or frequencia < 0 or frequencia > 100:
    print("Valores inválidos para nota ou frequência. Por favor, insira valores entre 0 e 100.")
else:
    # Primeira camada de verificação: nota alta e alta frequência
    if nota >= 90 and frequencia >= 90:
        print("Aprovado com Honras")
    # Segunda camada: nota e frequência em níveis aceitáveis para aprovação simples
    elif nota >= 70 and frequencia >= 75:
        print("Aprovado")
    # Terceira camada: possibilidade de recuperação (nota ou frequência abaixo dos padrões de aprovação)
    elif (50 <= nota < 70) or (50 <= frequencia < 75):
        # Neste bloco, analisamos individualmente as razões para a recuperação
        if nota < 70 and frequencia < 75:
            print("Recuperação: nota e frequência abaixo do ideal.")
        elif nota < 70:
            print("Recuperação: a nota está abaixo do ideal.")
        else:
            print("Recuperação: a frequência está abaixo do ideal.")
    # Caso nenhuma condição anterior seja satisfeita, o estudante é reprovado
    else:
        print("Reprovado")

"""
EXPLICAÇÃO DETALHADA:
1. Primeiro, o programa solicita os dados do estudante: a nota e a frequência.
2. Verifica se os valores estão no intervalo válido (0 a 100). Se não estiverem, informa erro.
3. Em seguida, utiliza condicionais aninhadas:
    - Se a nota for 90 ou mais e a frequência for 90% ou mais, o estudante é aprovado com honras.
    - Se a nota for 70 ou mais e a frequência for 75% ou mais, o estudante é aprovado.
    - Se a nota estiver entre 50 e 69 ou a frequência estiver entre 50 e 74, o estudante vai para recuperação.
      Dentro deste bloco, o código detalha se a deficiência se deve à nota, à frequência ou a ambos.
    - Em qualquer outro caso, o estudante é reprovado.
4. Cada bloco condicional é comentado para facilitar o entendimento dos jovens programadores.
"""
