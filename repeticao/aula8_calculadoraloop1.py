import os
while True:
    print("\n*** Calculadora de Números Reais ***")
    print("0. Fechar")
    print("1. Soma")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")
    print("*******************************************")

    op = int(input("Escolha a operação desejada: "))
    if op == 0:
        break
    elif op < 1 or op > 4:
        print("Operação inválida!")
    else:
        n1 = float(input("Digite o número 1: "))
        n2 = float(input("Digite o número 2: "))

        if op == 1:
            resultado = n1 + n2
        elif op == 2:
            resultado = n1 - n2
        elif op == 3:
            resultado = n1 * n2
        elif op == 4:
            if n2 == 0:
                print("Erro. Divisão por zero!")
                resultado = 0
            else:
                resultado = n1 / n2

        print(f"O resultado é: {resultado:.2f}")
        input("Tecle ENTER para continuar...")
        os.system("clear")
print("Programa fechado.")