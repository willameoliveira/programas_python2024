produtos = []
produtos.append(input("Nome do produto: "))
produtos.append(float(input("Digite o preço: ")))
produtos.append(int(input("Digite o estoque: ")))
produtos.append(input("Em promoção? (S|N): ").upper() == "S")

print("\nDados do produto")
print(f"Nome.......: {produtos[0]}")
print(f"Preço......: {produtos[1]}")
print(f"Estoque....: {produtos[2]}")
if produtos[3]: # igual a: if produtos[3] == True:
    print(f"Em promoção: Sim")
else:
    print("Em promoção: Não")