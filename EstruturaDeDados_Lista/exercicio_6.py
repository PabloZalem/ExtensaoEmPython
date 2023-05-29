import random

# Gerando a lista de números aleatórios para a Mega-Sena
numeros_jogados = random.sample(range(1, 61), 6)

# Solicitando ao usuário os números sorteados
numeros_sorteados = []
for i in range(6):
    numero = int(input("Digite o número sorteado: ")) # type: ignore
    numeros_sorteados.append(numero)

# Verificando a quantidade de números acertados
acertos = len(set(numeros_jogados).intersection(numeros_sorteados))

# Imprimindo os números jogados e a quantidade de acertos
print("Números jogados:", numeros_jogados)
print("Quantidade de acertos:", acertos)
