while True:
    matricula = int(input("Digite a matrícula do aluno (ou um número negativo para sair): "))
    
    if matricula < 0:
        break
    
    nota1 = float(input("Digite a primeira nota do aluno: "))
    nota2 = float(input("Digite a segunda nota do aluno: "))
    nota3 = float(input("Digite a terceira nota do aluno: "))
    
    media = (nota1 + nota2 + nota3) / 3
    
    if media >= 70:
        situacao = "Aprovado"
    elif media >= 60:
        situacao = "Exame"
    else:
        situacao = "Reprovado"
    
    print("Situação do aluno:", situacao)
    print()  # Linha em branco para separar as saídas dos diferentes alunos

print("Programa encerrado.")
