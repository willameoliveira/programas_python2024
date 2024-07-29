print("""       *** Bem vindo a Calculadora ***""")
comando = input("""
    Digite a operação desejada usando apenas dois números reais 
    (OBS: Utilize espaços entre os números e a operação): """)

partes = comando.split()
numero1 = float(partes[0])
operacao = partes[1]
numero2 = float(partes[2])

if operacao == "+":
    print (f"= {numero1 + numero2}") 
elif operacao == "-":
    print (f"= {numero1 - numero2}") 
elif operacao == "x":
    print (f"= {numero1 * numero2}") 
elif operacao == "/":
    if numero2 != 0:
        print (f"= {numero1 / numero2}") 
    else:
        print("Divisão por zero!")
else:
    print("Operação inválida!")