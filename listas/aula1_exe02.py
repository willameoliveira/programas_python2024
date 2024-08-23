eletronicos = []
while True:
    nome = input("Nome do eletrônico: ")
    eletronicos.append(nome)
    resp = input("Deseja adicionar outro? (s|n): ").upper()
    if resp == "N":
        break

print(eletronicos)