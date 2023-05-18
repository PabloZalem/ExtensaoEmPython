import math

def resolver_equacao_segundo_grau(a, b, c):
    delta = b**2 - 4*a*c

    if delta < 0:
        return None
    elif delta == 0:
        x = -b / (2*a)
        return x
    else:
        x1 = (-b + math.sqrt(delta)) / (2*a)
        x2 = (-b - math.sqrt(delta)) / (2*a)
        return x1, x2

print("Programa para resolver equação de segundo grau")
a = float(input("Digite o valor de a: "))
b = float(input("Digite o valor de b: "))
c = float(input("Digite o valor de c: "))

resultado = resolver_equacao_segundo_grau(a, b, c)

if resultado is None:
    print("A equação não possui raiz real.")
elif isinstance(resultado, tuple):
    x1, x2 = resultado
    print("As raízes da equação são:", x1, "e", x2)
else:
    x = resultado
    print("A raiz da equação é:", x)
