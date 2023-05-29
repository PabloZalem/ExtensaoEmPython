frase = input("Digite uma frase: ")
palavra = input("Digite uma palavra: ")

# Converter a frase e a palavra para minúsculas
frase = frase.lower()
palavra = palavra.lower()

# Contar a quantidade de vezes que a palavra aparece na frase
quantidade = frase.count(palavra)

# Imprimir o resultado
print("A palavra '{}' aparece {} vezes na frase.".format(palavra, quantidade))
