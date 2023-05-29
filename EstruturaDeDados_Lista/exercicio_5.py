meses = {
    1: "janeiro",
    2: "fevereiro",
    3: "março",
    4: "abril",
    5: "maio",
    6: "junho",
    7: "julho",
    8: "agosto",
    9: "setembro",
    10: "outubro",
    11: "novembro",
    12: "dezembro"
}

data = input("Digite uma data no formato DD/MM/AAAA: ")

# Separando o dia, mês e ano da data informada
dia, mes, ano = map(int, data.split('/'))

# Imprimindo a data por extenso
data_extenso = f"{dia} de {meses[mes]} de {ano}"
print(data_extenso)
