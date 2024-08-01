estatura1 = float(input("Informe a primeira estatura:"))
estatura2 = float(input("Informe a segunda estatura:"))
estatura3 = float(input("Informe a terceira estatura:"))

if estatura1 == estatura2 or estatura1 == estatura3 or estatura2 == estatura3:
    print("Há, pelo menos, duas pessoas com a mesma estatura")
else:
    maior_estatura = estatura1
    if estatura2 > maior_estatura:
        maior_estatura = estatura2
    if estatura3 > maior_estatura:
        maior_estatura = estatura3
    print(f"A maior estatura é:{maior_estatura}")