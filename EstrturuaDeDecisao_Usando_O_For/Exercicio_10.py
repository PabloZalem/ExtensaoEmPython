numero = int(input("Digite um número inteiro: "))

# Verifica se o número é menor que 2, pois números menores que 2 não são primos
if numero < 2:
    print(numero, "não é um número primo.")
else:
    eh_primo = True
    for i in range(2, numero):
        if numero % i == 0:
            eh_primo = False
            break

    if eh_primo:
        print(numero, "é um número primo.")
    else:
        print(numero, "não é um número primo.")
