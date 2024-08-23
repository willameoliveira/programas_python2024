import os
produtos = []

def imprimir(p):
  print("\n....................")
  print(f"Nome.......: {p[0]}")
  print(f"Preço......: {p[1]}")
  print(f"Estoque....: {p[2]}")
  print(f"Em promoção: { 'Sim' if p[3] else 'Não' }")
  
def cadastrar():
  resposta = 'S'   
  while resposta == 'S':
    os.system("clear")
    print("*** Cadastrar produto ***")
    nome = input("Nome: ")
    preco = float(input("Preço: "))
    estoque = int(input("Estoque: "))
    promocao = input("Em promoção? (s|n): ").upper() == 'S'
    produtos.append([nome, preco, estoque, promocao])
    print("\nProduto adicionado com sucesso!")
    resposta = input("Deseja adicionar outro? (s|n): ").upper()

def listar():
  os.system("clear")
  print("*** Produtos cadastrados ***")
  for produto in produtos:
    imprimir(produto)

def pesquisar(nomeProduto):
    produto_encontrado = None
    
    # Buscar o produto na lista
    for i, produto in enumerate(produtos):
        if produto[0].lower() == nomeProduto.lower():
            produto_encontrado = i
            break
    
    # Se o produto for encontrado
    if produto_encontrado is not None:
        produto = produtos[produto_encontrado]
        print("\nProduto encontrado:")
        imprimir(produto)

    return produto_encontrado

def alterar():
    os.system("clear")
    print("*** Alterar produto ***")
    
    nome = input("Digite o nome do produto que deseja alterar: ")
    produto_encontrado = pesquisar(nome)
    
    # Se o produto for encontrado
    if produto_encontrado is not None:
        produto = produtos[produto_encontrado]
        
        # Perguntar o que o usuário deseja alterar
        novo_nome = input(f"Novo nome [{produto[0]}]: ") or produto[0]
        novo_preco = input(f"Novo preço [{produto[1]}]: ")
        novo_estoque = input(f"Novo estoque [{produto[2]}]: ")
        nova_promocao = input(f"Em promoção? (s|n) [{ 'S' if produto[3] else 'N' }]: ").upper()
        
        # Atualizar os valores do produto
        produtos[produto_encontrado][0] = novo_nome
        produtos[produto_encontrado][1] = float(novo_preco) if novo_preco else produto[1]
        produtos[produto_encontrado][2] = int(novo_estoque) if novo_estoque else produto[2]
        produtos[produto_encontrado][3] = (nova_promocao == 'S') if nova_promocao else produto[3]
        
        print("\nProduto alterado com sucesso!")
    else:
        print("Produto não encontrado.")

def remover():
    os.system("clear")
    print("*** Remover produto ***")
    
    nome = input("Digite o nome do produto que deseja remover: ")
    produto_encontrado = pesquisar(nome)
    
    # Se o produto for encontrado
    if produto_encontrado is not None:
        produto = produtos[produto_encontrado]
        
        # Confirmar a remoção
        confirmacao = input("Tem certeza que deseja remover este produto? (s|n): ").upper()
        if confirmacao == 'S':
            produtos.pop(produto_encontrado)
            print("\nProduto removido com sucesso!")
        else:
            print("\nRemoção cancelada.")
    else:
        print("Produto não encontrado.")