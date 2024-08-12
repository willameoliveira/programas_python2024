erros = 0
nome = input("Informe seu nome: ")
while erros < 3:
    senha = input("Informe sua senha: ")
    if senha == "123456":
        print(f"Olá, {nome}. Seja bem vindo ao nosso banco.")
        break
    else:
        erros+=1
        if erros < 3:
            print(f"Senha incorreta! Você ainda tem {3 - erros} tentativa(s).")
        else:
            print("Sua senha foi bloqueada! Por favor, dirija-se a um de nossos caixas.")