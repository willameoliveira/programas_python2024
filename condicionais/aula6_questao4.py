usuario = input("Digite o nome de usuário: ").lower()
senha = input("Digite sua senha: ")

if (usuario == "procopio" and senha == "12345") or (usuario == "paiva" and senha == "54321"):
    print("Seja bem vindo!")
else:
    print("Usuário e/ou senha não conferem!")