salario_total = 0
num_filhos_total = 0
num_habitantes = 0

salario = float(input("Digite o salário (digite um número negativo para sair): "))
while salario >= 0:
    num_filhos = int(input("Digite o número de filhos: "))
    
    salario_total += salario
    num_filhos_total += num_filhos
    num_habitantes += 1
    
    salario = float(input("Digite o salário (digite um número negativo para sair): "))

if num_habitantes > 0:
    media_salario = salario_total / num_habitantes
    media_filhos = num_filhos_total / num_habitantes
    
    print("Média do salário da população: ", media_salario)
    print("Média do número de filhos: ", media_filhos)
else:
    print("Nenhum dado foi inserido.")
