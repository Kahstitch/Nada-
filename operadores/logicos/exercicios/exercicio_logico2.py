# -----------------------------------------------------
# Exercício: Verificação de Acesso a Conta Bancária
# -----------------------------------------------------

# O usuário só pode acessar a conta se:
# 1. Ele souber a senha correta.
# 2. Ele estiver usando um dispositivo confiável OU inserir um código de verificação.

# Definição da senha correta
senha_correta = "Python123"

# Pergunta ao usuário a senha
senha_digitada = input("Digite sua senha: ")

# Verifica se a senha está correta
senha_valida = senha_digitada == senha_correta

# Pergunta se está em um dispositivo confiável
dispositivo_confiavel = input("Este é um dispositivo confiável? (s/n): ").strip().lower() == "s"

# Pergunta o código de verificação caso o dispositivo NÃO seja confiável
if not dispositivo_confiavel:
    codigo_verificacao = input("Digite o código de verificação enviado ao seu e-mail: ")
    codigo_correto = "4321"  # Código fictício para simulação
    codigo_valido = codigo_verificacao == codigo_correto
else:
    codigo_valido = True  # Se o dispositivo for confiável, o código é automaticamente válido

# Verifica se o usuário pode acessar a conta
acesso_permitido = senha_valida and (dispositivo_confiavel or codigo_valido)

# Exibe a mensagem correspondente
if acesso_permitido:
    print("Acesso permitido: Bem-vindo à sua conta!")
else:
    print("Acesso negado: Senha ou código de verificação incorretos.")

# Explicação:
# - `senha_digitada == senha_correta`: Garante que a senha esteja correta.
# - `dispositivo_confiavel`: Se for "s", ignora a necessidade de código de verificação.
# - `not dispositivo_confiavel`: Se for "n", exige um código de verificação correto.
# - `acesso_permitido = senha_valida and (dispositivo_confiavel or codigo_valido)`: 
#    → O usuário precisa da senha correta **E** estar em um dispositivo confiável **OU** inserir um código válido.
