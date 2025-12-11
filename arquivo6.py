# CARREGAR UM ARQUIVO EXISTENTE PARA LISTA
# ADICIONAR NOVOS ITENS NA LISTA
# GRAVAR A LISTA COMPLETA SOBREPONDO O ARQUIVO

arq = open("carros.txt", "r")
carros = arq.readlines()
arq.close()

for x in range(5):
    c = input("Digite um carro:")
    carros.append(c + "\n")

carros.sort()

arq = open("carros.txt", "w")
arq.writelines(carros)
arq.close()
print("Gravado com sucesso.")