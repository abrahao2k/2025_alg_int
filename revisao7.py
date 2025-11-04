# SABER A POSIÇÃO DE UM ELEMENTO

cores = ["azul","verde","branco","cinza"]

#print("Pos:", cores.index("verde"))

pesq = input("Digite uma cor:")

if pesq in cores:
    print("Pos:", cores.index(pesq))

else:
    print("Não existe na lista.")

