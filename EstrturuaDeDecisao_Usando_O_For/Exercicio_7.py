soma_pesos = 0

for i in range(1, 11):
    peso = float(input("Digite o peso da pessoa {}: ".format(i)))
    soma_pesos += peso

media_pesos = soma_pesos / 10

print("A média dos pesos é:", media_pesos)
