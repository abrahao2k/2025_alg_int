# DICIONÁRIO DE DADOS

aluno = {"nome"   : "Ana",
         "curso"  : "Informática",
         "cidade" : "Mossoró"}

     # chave(key)   # valor(value)

print(aluno)

print(aluno["nome"])
print(aluno["curso"])
print(aluno["cidade"])

aluno["turno"] = "Manhã"  # adicionar novas informações

print(aluno)

del(aluno["cidade"])  # apagar uma informação

print(aluno)

lista = list(aluno.values())  # convertendo para lista
print(lista)
