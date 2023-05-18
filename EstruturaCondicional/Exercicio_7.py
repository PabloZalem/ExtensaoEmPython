peso = float(input("Informe o peso em kg: "))
altura = float(input("Informe a altura em metros: "))

imc = peso / (altura ** 2)

print("O IMC calculado é:", imc)

if imc < 18.5:
    situacao_peso = "Abaixo do peso"
elif imc < 25:
    situacao_peso = "Peso normal"
elif imc < 30:
    situacao_peso = "Sobrepeso"
elif imc < 35:
    situacao_peso = "Obesidade Grau I"
elif imc < 40:
    situacao_peso = "Obesidade Grau II (severa)"
else:
    situacao_peso = "Obesidade Grau III (mórbida)"

print("Situação do peso:", situacao_peso)
