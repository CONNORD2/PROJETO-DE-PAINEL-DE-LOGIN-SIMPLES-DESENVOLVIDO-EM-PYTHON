def verificar_usuario(usuario):
    if usuario.upper() == "ADMINISTRADOR":  # Usar .upper() para tornar a comparação insensível a maiúsculas/minúsculas
        return True
    else:
        return False

def verificar_senha(senha):
    if senha == "love you":
        return True
    else:
        return False

# Solicitar entrada do usuário
usuario = input("QUAL O SEU USUÁRIO: ")
senha = input("QUAL A SUA SENHA: ")

# Verificar usuário e senha
if verificar_usuario(usuario) and verificar_senha(senha):
    print("ACESSO CONCEDIDO")
else:
    print("USUÁRIO OU SENHA INCORRETOS")
