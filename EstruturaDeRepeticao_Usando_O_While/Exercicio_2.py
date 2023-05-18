contador = 0
soma_idades = 0
acima_50 = 0
abaixo_40 = 0

while True:
    idade = int(input("Digite a idade (ou um número negativo para sair): "))
    
    if idade < 0:
        break
    
    contador += 1
    soma_idades += idade
    
    if idade > 50:
        acima_50 += 1
    
    if idade < 40:
        abaixo_40 += 1

if contador > 0:
    media_idades = soma_idades / contador
    percentual_abaixo_40 = (abaixo_40 / contador) * 100
else:
    media_idades = 0
    percentual_abaixo_40 = 0

print("Quantidade de pessoas acima de 50 anos:", acima_50)
print("Média de idade das pessoas:", media_idades)
print("Percentual de pessoas abaixo de 40 anos:", percentual_abaixo_40, "%")
