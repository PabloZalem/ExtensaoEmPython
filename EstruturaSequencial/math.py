import math
x = int(input("Digite um número:"))
y = math.sqrt(x)
z = math.pow(x, 3)

print("Raiz:", y)
print("Potência:", z)
print("1 - Raiz de", x, "=", y)
print("2 - Raiz de " + str(x) + " = " + str(y))
print("3 - Raiz de %r = %r" %(x, y))
print("4 - Raiz de %r = %f" %(x, y))
print("5 - Raiz de %r = %.2f" %(x, y))
print(f"6 - Raiz de {x} = {y}")
print(f"7 - Raiz de {x} = {y:.2f}")
