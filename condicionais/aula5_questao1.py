n1 = int(input("Digite um número inteiro positivo: "))

if n1 <= 0:
    print("Informe um número inteiro positivo!")
else:
    if n1 % 2 == 0: 
        print(f"quadrado de {n1} = {n1**2}") 
    else:
        print(f"cubo de {n1} = {n1**3}")