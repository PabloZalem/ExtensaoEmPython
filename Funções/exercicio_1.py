def dobro_numero(numero):
    return numero * 2

def maior_numero(numero1, numero2):
    return max(numero1, numero2)

def fatorial(numero):
    resultado = 1
    for i in range(1, numero + 1):
        resultado *= i
    return resultado

def soma_elementos(numero):
    return sum(range(1, numero + 1))

def verificar_par(numero):
    if numero % 2 == 0:
        return True
    else:
        return False

# Exemplos de uso das funções
print(dobro_numero(5))  # Saída: 10
print(maior_numero(8, 3))  # Saída: 8
print(fatorial(4))  # Saída: 24
print(soma_elementos(10))  # Saída: 55
print(verificar_par(7))  # Saída: False
print(verificar_par(10))  # Saída: True
