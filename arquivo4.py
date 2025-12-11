# GRAVAR UMA LISTA EM UM ARQUIVO

carros = []

for x in range(5):
    c = input("Digite um carro:")
    carros.append(c + "\n")

carros.sort() # ordem alfabética

arq = open("carros.txt","w")
arq.writelines(carros)       # grava a lista inteira no arquivo
arq.close()
print("Gravado com sucesso.")

