import random

# Criando a lista original com 10 valores inteiros aleatórios
lista_original = [random.randint(1, 100) for _ in range(10)]

# Criando as listas para armazenar os valores pares e ímpares
lista_pares = []
lista_impares = []

# Separando os valores pares e ímpares
for valor in lista_original:
    if valor % 2 == 0:
        lista_pares.append(valor)
    else:
        lista_impares.append(valor)

# Imprimindo as três listas
print("Lista original:", lista_original)
print("Lista de pares:", lista_pares)
print("Lista de ímpares:", lista_impares)
