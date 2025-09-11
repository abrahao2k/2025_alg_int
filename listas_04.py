# crie um programa que solicita a digitação do nome de 10 pessoas,
# armazena-os em uma lista e exibe a lista

# 1. criar uma lista vazia
nomes = []

# 2. laço que repete 10x
cont = 1
while cont <= 10 :
    dig = input("Digite o nome: ")
    
    # 3. acrescentar na lista
    nomes.append(dig)
    
    cont += 1

# 4. exibir a lista
print(nomes)