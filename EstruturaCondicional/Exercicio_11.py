numero = int(input("Digite um número inteiro entre 1 e 12: "))

if numero == 1:
    mes = "Janeiro"
elif numero == 2:
    mes = "Fevereiro"
elif numero == 3:
    mes = "Março"
elif numero == 4:
    mes = "Abril"
elif numero == 5:
    mes = "Maio"
elif numero == 6:
    mes = "Junho"
elif numero == 7:
    mes = "Julho"
elif numero == 8:
    mes = "Agosto"
elif numero == 9:
    mes = "Setembro"
elif numero == 10:
    mes = "Outubro"
elif numero == 11:
    mes = "Novembro"
elif numero == 12:
    mes = "Dezembro"
else:
    mes = "Não existe mês com este número"

print("Mês: " + mes)
