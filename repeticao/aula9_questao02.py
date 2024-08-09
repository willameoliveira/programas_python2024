primeiro_termo = int(input("escreva o primeiro termo: "))
quant_de_termos = int(input("escreva quantidade de termos: "))
raz = int(input("escreva a razao: "))

ultimo_termo = primeiro_termo + (quant_de_termos-1)*raz
for termo in range(primeiro_termo, ultimo_termo+1, raz):
  print(termo)
print('Fim')