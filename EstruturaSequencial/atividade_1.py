'''
1.	Leia três números inteiros e imprima a média aritmética entre esses números.
'''
sum = 0
for i in range(0,3):
    i = int(input('Digite um valor: '))
    sum = sum + i

print('A média dos tres numeros: ', (sum/3))