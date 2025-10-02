alunos = []  # lista principal

while True:
    nome = input("Nome do aluno: ")
    curso = input("Curso: ")
    
    alunos.append( [nome, curso] )   # sub-lista
    
    resp = input("Outro cadastro? s/n ")
    if resp == 'n' : break

print("## ALUNOS CADASTRADOS ##")
print(alunos)

print(alunos[2][0]) # nome do aluno na sub-lista 2
print(alunos[1][1]) # curso do aluno na sub-lista 1
