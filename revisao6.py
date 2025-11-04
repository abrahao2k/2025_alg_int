# VERIFICAR SE UMA POSIÇÃO EXISTE NA LISTA
cores = ["azul","verde","branco","cinza"]
print("Qdt. itens:", len(cores)) # conta itens da lista

pos = int(input("Digite uma posição: "))

if pos < len(cores) :
    print("Posição existe.")
    cores.pop(pos)
else:
    print("Posição inválida.")