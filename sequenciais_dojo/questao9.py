from math import sqrt
n1= int(input("digite um numero inteiro: "))
n2= int(input("digite um numero inteiro: "))

cubo = n2**3
mediag = sqrt(n1*n2)
print(f"""o cubo do 2n {cubo} é a media geometrica entre {n1} e {n2} é igual a:{(mediag):.2f}""" )