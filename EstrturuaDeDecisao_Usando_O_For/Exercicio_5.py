numero = int(input("Digite um número inteiro: "))

# Verifica se o número é negativo
if numero < 0:
    print("O fatorial não está definido para números negativos.")
elif numero == 0:
    print("O fatorial de 0 é 1.")
else:
    fatorial = 1
    for i in range(1, numero + 1):
        fatorial *= i

    print("O fatorial de", numero, "é", fatorial)
