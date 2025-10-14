'''4. Crie um programa que pergunta quantos alunos
participam de uma classe. Use um laço 
for para solicitar a digitação do nome e da nota
para cada aluno, armazenando tudo em 
uma lista. Após a digitação, percorra a lista
(usando um laço for) e imprima frases com o 
nome, nota e resultado do aluno, de acordo com
as regras abaixo.
De 60 a 100 – aprovado.
De 40 a 59 – em recuperação.
Abaixo de 40 – reprovado.
'''

qtd = int(input("Quantos alunos? "))
alunos = []

for num in range(qtd):
    nome = input("Nome: ")
    nota = int(input("Nota:"))
    alunos.append( [nome,nota] ) #sub-lista
    
for pessoa in alunos :
    if pessoa[1] >= 60 :
        print(pessoa[0],pessoa[1],"Aprovado")
    elif pessoa[1] >= 40 :
        print(pessoa[0],pessoa[1],"Recuperação")
    else:
        print(pessoa[0],pessoa[1],"Reprovado")
    
    
    
