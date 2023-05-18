idade = int(input('Digite sua idade: '))

while(idade < 0):
    idade = int(input('Idade inválida! Digite novamente: '))

print('idade válida: ', idade)