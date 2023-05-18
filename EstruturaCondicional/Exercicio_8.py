idade = int(input("Digite a idade do nadador: "))

if idade <= 7:
    categoria = "INFANTIL"
elif idade <= 10:
    categoria = "JUVENIL"
elif idade <= 15:
    categoria = "ADOLESCENTE"
else:
    categoria = "ADULTO"

print("Categoria: " + categoria)