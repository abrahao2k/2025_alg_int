'''Exercício 3: Nomes em uma Lista
Peça ao usuário para inserir nomes em uma lista usando
um loop "while". Continue pedindo nomes até que o usuário
insira a palavra "fim" (não entra na lista). Em seguida,
exiba a lista de nomes.'''

nomes = list()

dig = ""
while dig != "fim" :
    dig = input("Digite o nome: ")
    
    if dig.lower() != "fim" :   # lower() transforma em minúsculas
        nomes.append(dig)

else:
    print("Nomes digitados: ", nomes)

