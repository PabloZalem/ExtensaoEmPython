numero = int(input("Digite um número: "))

print("Números ímpares até", numero, ":")

for i in range(1, numero+1):
    if i % 2 != 0:
        print(i)
