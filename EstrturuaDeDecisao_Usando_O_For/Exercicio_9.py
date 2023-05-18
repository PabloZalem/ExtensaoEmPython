quantidade_peso_maior_90 = 0
soma_idades = 0

for i in range(1, 8):
    idade = int(input("Digite a idade da pessoa {}: ".format(i)))
    peso = float(input("Digite o peso da pessoa {}: ".format(i)))

    if peso > 90:
        quantidade_peso_maior_90 += 1

    soma_idades += idade

media_idades = soma_idades / 7

print("Quantidade de pessoas com mais de 90 kg:", quantidade_peso_maior_90)
print("Média das idades:", media_idades)
