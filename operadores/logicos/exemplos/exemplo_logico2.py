# ---------------------------------------------
# Exemplo Avançado de Operadores Lógicos
# ---------------------------------------------

# Simulação de um sistema de controle de acesso baseado em idade e permissão dos pais

# Pergunta ao usuário a idade e se tem autorização dos pais
idade = int(input("Digite sua idade: "))
tem_autorizacao_pais = input("Possui autorização dos pais? (s/n): ").strip().lower() == "s"

# Definição das regras
# - Pode entrar sozinho se tiver 18 anos ou mais
# - Pode entrar com autorização dos pais se tiver entre 13 e 17 anos
# - Não pode entrar se tiver menos de 13 anos

pode_entrar_sozinho = idade >= 18
pode_entrar_com_pais = 13 <= idade < 18 and tem_autorizacao_pais
nao_pode_entrar = idade < 13

# Verificação e exibição da mensagem adequada
if pode_entrar_sozinho:
    print("Acesso permitido: Você pode entrar sozinho.")
elif pode_entrar_com_pais:
    print("Acesso permitido: Você pode entrar com autorização dos pais.")
else:
    print("Acesso negado: Você não pode entrar.")

# Explicação:
# - `idade >= 18`: Permite entrada livre para maiores de idade.
# - `13 <= idade < 18 and tem_autorizacao_pais`: Permite entrada com autorização.
# - `idade < 13`: Bloqueia acesso para crianças menores de 13 anos.
