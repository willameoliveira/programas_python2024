a = int(input("Digite uma número inteiro: "))
b = int(input("Digite uma número inteiro: "))

soma = 0
if a < b:
    for termo in range(a,b+1):
         soma+= termo
    print(soma)
else:
    print("Erro, tente novamente.")