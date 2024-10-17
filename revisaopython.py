nota1 = float(input("Digite a nota 1: "))
nota2 = float(input("Digite a nota 2: "))
nota3 = float(input("Digite a nota 3: "))
media = (nota1 + nota2 + nota3) / 3

print(f"Média do aluno: {media:.1f}")

if media >= 7:
    print("Resultado: Aluno aprovado.")
elif media >= 4:
    print("Resultado: Aluno de prova final.")
else:
    print("Resultado: Aluno reprovado.")