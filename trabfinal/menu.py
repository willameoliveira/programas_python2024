import os, produto

os.system("clear")
while True:
    print("*** Bem vindo ao sistema de vendas ***")
    print("1 - Cadastrar produto")
    print("2 - Listar produtos")
    print("3 - Alterar produto")
    print("4 - Remover produto")
    print("5 - Pesquisar produto")
    print("5 - Realizar venda")
    print("6 - Listar vendas")
    print("7 - Sair")
    op = int(input("\nEscolha a opção: "))
    if op == 1:
        produto.cadastrar()
    elif op == 2:
        produto.listar()
    elif op == 3:
        produto.alterar()
    elif op == 4:
        produto.remover()
    elif op == 5:
        nome = input("Digite o nome do produto que deseja pesquisar: ")
        produto.pesquisar(nome)
    elif op == 7:
        print("Programa fechado")
        break
    
    input("\nTecle ENTER para continuar...")
    os.system("clear")