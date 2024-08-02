op = 1 # valor de inicialização
while op != 0:
  print("\n*** Calculadora de Números Reais ***")
  print("0. Fechar")
  print("1. Soma")
  print("2. Subtração")
  print("3. Multiplicação")
  print("4. Divisão")
  print("*******************************************")
  op = int(input("Escolha a operação desejada: "))

  if op in (1, 2, 3, 4): # op == 1 or op == 2 or op == 3 or op == 4
    n1 = float(input("Digite o número 1: "))
    n2 = float(input("Digite o número 2: "))
    
    if op == 1:
        resultado = n1 + n2
    elif op == 2:
        resultado = n1 - n2
    elif op == 3:
        resultado = n1 * n2
    elif op == 4:
        resultado = n1 / n2

    print(f"O resultado é: {resultado:.2f}")
  elif op < 0 or op > 4:
     print("Operação inválida!")
  else: # se a pessoa digitar zero
     print("Programa fechado.")