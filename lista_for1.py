'''1. Crie um programa que use um laço for
para solicitar a digitação do nome de 5 alunos. 
Após a digitação, exiba a lista.'''

alunos = list()

for num in range(5):
    nome = input("Nome do aluno: ")
    alunos.append(nome)
    print("Aluno incluido na lista.\n")

print("== RELAÇÃO DE ALUNOS ==")
#print(alunos)
for nome in alunos: print(nome)