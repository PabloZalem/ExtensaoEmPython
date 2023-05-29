import random


lista = random.sample(range(1, 21), 10)
print("Lista original:", lista)

maior_valor = max(lista)
print("Maior valor:", maior_valor)

menor_valor = min(lista)
print("Menor valor:", menor_valor)

soma_valores = sum(lista)
print("Soma dos valores:", soma_valores)

media_valores = soma_valores / len(lista)
print("Média dos valores:", media_valores)

lista_ordenada_crescente = sorted(lista)
print("Lista em ordem crescente:", lista_ordenada_crescente)

lista_ordenada_decrescente = sorted(lista, reverse=True)
print("Lista em ordem decrescente:", lista_ordenada_decrescente)

valor = int(input("Digite um valor: "))

ocorrencias = lista.count(valor)
if ocorrencias > 0:
    print("O valor", valor, "ocorre", ocorrencias, "vezes na lista.")
else:
    print("O valor", valor, "não se encontra na lista.")