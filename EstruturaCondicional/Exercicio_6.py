sexo = int(input("Informe o sexo (1 para homens, 2 para mulheres): "))
altura = float(input("Informe a altura em metros: "))

if sexo == 1:
    peso_ideal = (72.7 * altura) - 58
    print("O peso ideal para homens é:", peso_ideal)
elif sexo == 2:
    peso_ideal = (62.1 * altura) - 44.7
    print("O peso ideal para mulheres é:", peso_ideal)
else:
    print("Opção inválida. Informe 1 para homens ou 2 para mulheres.")
