'''
4.	Leia um número e imprima a tabuada de multiplicar deste número. Por exemplo, para o número 5: python
'''
numero=int(input("Qual tabuada voce quer saber? Digite um numero de 1 a 10.\n"))

print(" Tabuada do ",numero,":\n")
for i in range(1,11):
    print(numero," X ",i," = ",numero*i, "\n")