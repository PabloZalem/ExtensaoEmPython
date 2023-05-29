palavra = input("Digite uma palavra: ")
separador = input("Informe um caractere separador: ")

# Incluir o separador entre cada letra da palavra
palavra_separada = separador.join(palavra)

# Imprimir o resultado
print("Palavra separada:", palavra_separada)
