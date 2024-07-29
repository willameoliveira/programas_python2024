comissao= 200

nome = input("Digite seu nome: ")
imv_ven = int(input("Digite quantos imóveis foram vendidos: "))
total_vendas = float(input("Digite o total das vendas: "))
salario_minimo = 1500 + comissao * imv_ven + total_vendas * 0.05
print(f"seu salario é: {salario_minimo}")