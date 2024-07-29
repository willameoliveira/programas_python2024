print("plano 1")

x1 = float(input("Digite o valor de x1 no plano 1: "))
y1 = float(input("Digite o valor de y1 no plano 1: "))

print("plano 2")

x2 = float(input("Digite o valor de x2 no plano 2: "))
y2 = float(input("Digite o valor de y2 no plano 2: "))
import math 
resultado= (x2-x1)**2 + (y2-y1)**2
resul2 = math.sqrt (resultado)
print ("A distância entre os pontos é de:", resul2)