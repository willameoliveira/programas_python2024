print(""""
      -------- Cargos -------------
      1. Programador de sistemas
      2. Analista de sistemas
      3. Analista de banco de dados
      """)
cargo = int(input("Digite o seu cargo: "))
if cargo < 1 or cargo > 3:
    print ("Cargo inválido")
else:    
    salario = float(input("Digite o seu salário: "))
    if cargo == 1:
        print(f"Seu novo salário é: {salario*1.3:.2f}")
    elif cargo == 2:
        print(f"Seu novo salário é: {salario*1.2:.2f}")
    elif cargo == 3:
        print(f"Seu novo salário é: {salario*1.15:.2f}")