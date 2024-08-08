soma = 0
quant = 0
maior = 0
num = int(input("Digite um número inteiro positivo: "))
while num > 0:
  soma += num
  quant += 1
  if num > maior:
    maior = num
  num = int(input("Digite um número inteiro positivo: "))
print(f"A soma é: {soma}")
media = soma / quant
print(f"a média é: {media:.2f}")
print(f"o maior é: {maior}")