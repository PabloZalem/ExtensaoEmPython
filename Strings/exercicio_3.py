frase = input("Digite uma frase: ")
caractere = input("Informe um caractere para dividir a frase: ")

# Dividir a frase em partes usando o caractere informado
partes = frase.split(caractere)

# Imprimir as partes resultantes
print("Frase dividida:")
for parte in partes:
    print(parte)
