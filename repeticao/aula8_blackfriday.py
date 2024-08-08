print("""
Loja de Perfume:
      Código:       Condição de Pagamento:              Desconto:
      0.            Parar o programa
      1.            À vista(em espécie)                 15%
      2.            Cartão de débito                    10%
      3.            Cartão de crédito(vencimento)       5%
""")

fp = 1
while fp != 0:
    
    tv = float(input("Informe o valor total da venda: "))
    fp = int(input("Informe a forma de pagamento\n'0' para Finalizar: "))

    if fp == 1:
        print(f"O valor final a ser pago é: {tv * 0.85}")
    elif fp == 2:
        print(f"O valor final a ser pago é: {tv * 0.90}")
    elif fp == 3:
        print(f"O valor final a ser pago é: {tv * 0.95}")
    elif fp < 0 or fp > 3:
        print("Forma de pagamento não encontrada")
    else:
        print("Programa encerrado.")