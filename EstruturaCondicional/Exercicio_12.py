def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b != 0:
        return a / b
    else:
        print("Não é possível dividir por zero.")
        return None

while True:
    print("== Calculadora ==")
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))

    print("Selecione a operação:")
    print("1 - Somar")
    print("2 - Subtrair")
    print("3 - Multiplicar")
    print("4 - Dividir")
    print("5 - Sair")

    opcao = int(input("Digite o número da operação desejada: "))

    if opcao == 1:
        resultado = somar(num1, num2)
        print("Resultado: ", resultado)
    elif opcao == 2:
        resultado = subtrair(num1, num2)
        print("Resultado: ", resultado)
    elif opcao == 3:
        resultado = multiplicar(num1, num2)
        print("Resultado: ", resultado)
    elif opcao == 4:
        resultado = dividir(num1, num2)
        if resultado is not None:
            print("Resultado: ", resultado)
    elif opcao == 5:
        print("Saindo do programa...")
        break
    else:
        print("Opção inválida. Por favor, digite uma opção válida.")
