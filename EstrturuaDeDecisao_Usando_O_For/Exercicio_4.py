numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))

menor = min(numero1, numero2)
maior = max(numero1, numero2)

print("Números entre", menor, "e", maior, ":")

for i in range(menor + 1, maior):
    print(i)
