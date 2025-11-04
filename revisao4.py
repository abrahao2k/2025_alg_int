# ALTERANDO UMA LISTA
# MODIFICAR UM ELEMENTO
cores = ["azul","verde","branco","cinza"]
          #0       1        2       3
print(cores)

cores[0] = "azul-marinho"
print(cores)

# REMOVER ELEMENTOS (PELO CONTEÚDO) / precisa existir
cores.remove("branco")
print(cores)

# REMOVER ELEMENTOS (PELA POSIÇÃO) / precisa existir
cores.pop(1)
print(cores)