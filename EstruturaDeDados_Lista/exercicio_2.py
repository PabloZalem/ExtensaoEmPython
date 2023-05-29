import random

# Criando as duas listas originais
lista1 = [random.randint(1, 100) for _ in range(10)]
lista2 = [random.randint(1, 100) for _ in range(10)]

# Criando as listas de soma e multiplicação
soma = [x + y for x, y in zip(lista1, lista2)]
multiplicacao = [x * y for x, y in zip(lista1, lista2)]

# Imprimindo as três listas
print("Lista 1:", lista1)
print("Lista 2:", lista2)
print("Soma:", soma)
print("Multiplicação:", multiplicacao)
