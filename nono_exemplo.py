"""
LOGIN SIMPLES
"""

usuario_correto = "admin" # Nome correto do usuario.
senha_correta = "1234" # Senha correta

while True:
    usuario = input("Nome de usuário: ")
    senha = input("Senha: ")
    
    if usuario == usuario_correto and senha == senha_correta: # Se o usuario e a senha forem corretas.
        print("Login bem-sucedido!") # O acesso será liberado.
        break # E o sistema irá parar.
    else:
        print("Usuário ou senha incorretos! Tente novamente.")