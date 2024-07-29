#Exercício 2 do Capítulo 3
opcao = int(input('''  
1. Média ponderada com pesos 2 e 3 
2. Quadrado da soma dos dois números
3. Cubo do menor número

Escolha uma das opções: 
'''))

if (opcao == 1 or opcao == 2 or opcao==3):
    num1 = float(input("Digite um número positivo: "))
    num2 = float(input("Digite outro número positivo: "))   

if opcao == 1:
    media_pond = (num1 * 2 + num2 * 3)/(2 + 3)
    print("A média ponderada de peso 2 e 3 do seu número é {:.2f}".format(media_pond))
elif opcao == 2:
    soma = (num1 + num2) ** 2
    print("O quadrado da soma dos dois números é {:.2f}".format(soma))
elif opcao ==3:
    if num1 < num2:
        cubo1 = num1 **3
        print("O cubo do seu menor número é {:.2f}".format(cubo1))
    else:
         cubo2 = num2 **3
         print("O cubo do seu menor número é {:.2f}".format(cubo2))
else:
    print("ERRO, opções da tabela não escolhida ")