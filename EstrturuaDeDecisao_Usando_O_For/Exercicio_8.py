homens_peso_correto = 0
mulheres_peso_correto = 0

for i in range(1, 11):
    sexo = input("Digite o sexo da pessoa {} (M para masculino, F para feminino): ".format(i))
    peso = float(input("Digite o peso da pessoa {}: ".format(i)))

    if sexo.upper() == "M" and peso >= 60 and peso <= 80:
        homens_peso_correto += 1
    elif sexo.upper() == "F" and peso >= 50 and peso <= 70:
        mulheres_peso_correto += 1

print("Quantidade de homens com peso entre 60 e 80 kg:", homens_peso_correto)
print("Quantidade de mulheres com peso entre 50 e 70 kg:", mulheres_peso_correto)
