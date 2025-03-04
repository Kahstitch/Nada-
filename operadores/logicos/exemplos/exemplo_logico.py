`python
# Exemplo de operadores lógicos em Python

# Declaração de variáveis booleanas
tem_carteira_motorista = True
tem_carro = False

# Uso do operador AND (E lógico)
# Só pode dirigir se tiver carteira de motorista E um carro
pode_dirigir = tem_carteira_motorista and tem_carro
print("Pode dirigir?", pode_dirigir)  # False

# Uso do operador OR (OU lógico)
# Pode viajar de carro se tiver um carro ou um amigo com carro
amigo_tem_carro = True
pode_viajar = tem_carro or amigo_tem_carro
print("Pode viajar?", pode_viajar)  # True

# Uso do operador NOT (Negação lógica)
# Se não tem carteira de motorista, não pode dirigir
nao_pode_dirigir = not tem_carteira_motorista
print("Não pode dirigir?", nao_pode_dirigir)  # False
