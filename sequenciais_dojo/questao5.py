import math
x1 = float(input("Digite o valor do primeiro x: "))
x2 = float(input("Digite o valor do segundo x: "))
y1 = float(input("Digite o valor do primeiro y: "))
y2 = float(input("Digite o valor do segundo y: "))

d = (x2 - x1) ** 2 + (y2 - y1) ** 2
print(f"a distancia é: {(math.sqrt(d)):.2f}")