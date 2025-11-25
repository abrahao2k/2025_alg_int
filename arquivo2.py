arq = open("alunos.txt","a") # a - append/acrescentar

nome = input("Nome do aluno: ")

arq.write(nome + "\n") # \n - para pular a linha

print("Gravado com sucesso.")

arq.close()