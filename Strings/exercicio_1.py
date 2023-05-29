frase = input("Digite uma frase: ")

# Transformar a frase em minúscula
frase_minuscula = frase.lower()
print("Frase em minúscula:", frase_minuscula)

# Frase na vertical
print("Frase na vertical:")
for letra in frase:
    print(letra)

# Solicitar posição inicial e final
posicao_inicial = int(input("Digite a posição inicial: "))
posicao_final = int(input("Digite a posição final: "))

# Imprimir parte da frase entre as posições informadas
parte_frase = frase[posicao_inicial:posicao_final + 1]
print("Parte da frase:", parte_frase)

# Frase em ordem inversa
frase_inversa = frase[::-1]
print("Frase em ordem inversa:", frase_inversa)

# Substituir palavras na frase
palavra1 = input("Digite a primeira palavra: ")
palavra2 = input("Digite a segunda palavra: ")

nova_frase = frase.replace(palavra1, palavra2)
print("Nova frase:", nova_frase)
