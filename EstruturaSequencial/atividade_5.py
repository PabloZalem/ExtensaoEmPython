'''
5.	Receba um número positivo, calcule e mostre:
a.	O número digitado ao quadrado
b.	O número digitado ao cubo
c.	A raiz quadrada do número digitado
d.	A raiz cúbica do número digitado.
'''
import math
tela = True

while tela == True:
    num1 = int(input('Digite um numero: '))

    if num1 > 0:
        quadrado = num1 * num1
        raiz = math.sqrt(num1)
        print(f'O numero digitado ao quadrado é: {quadrado}')
        print(f'A raiz do numero digitado é: {raiz}')
        tela = False
    elif num1 <= 0:
        print("numero invalido!")
        Tela = True