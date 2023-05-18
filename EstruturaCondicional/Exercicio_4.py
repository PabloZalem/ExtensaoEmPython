A = int(input("Digite o lado A:"))
B = int(input("Digite o lado B:"))
C = int(input("Digite o lado C:"))
if (A > (B + C)) or (B > (A+C)) or (C > (A+B)):
    print("Nao e um triangulo")
else:
    if (A == B == C):
        print("Triangulo Equilatero")
    elif (A != B and B == C) or (A != C and B == C) or (C != A and A==B):
        print("Triangulo Isosceles")
    else:
        print("Triangulo Escaleno")