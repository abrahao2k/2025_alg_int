# LER OS DADOS DE UM ARQUIVO PARA UMA LISTA

arq = open("carros.txt", "r")
carros = arq.readlines()   # põe cada linha do arq em uma posição na lista
arq.close()
print(carros)

# TIRAR OS \n DE CADA ITEM DA LISTA
lista = []
for c in carros:
    lista.append(c.strip("\n"))

print(lista)