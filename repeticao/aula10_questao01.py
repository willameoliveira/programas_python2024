#questão 3 cap IV
soma = 0
menor_preco = 0
mais_barato = None #inicializa o nome do mais barato com 'nada'
for cont in range(5):
  nome = input("Nome do medicamento: ")
  preco = float(input("Informe o valor: "))
  if cont == 0: # na primeira execução, o menor preço é iniciado com o preço do primeiro
    menor_preco = preco
  soma+=preco
  if (preco < menor_preco):
    menor_preco = preco
    mais_barato = nome
print(f"\nO mais barato é: {mais_barato} e o seu preço é R$ {menor_preco:.2f}")
print(f"A média aritmética dos preços é {soma/5:.2f}")