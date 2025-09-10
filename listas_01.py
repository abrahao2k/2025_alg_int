numeros = [35, 48, 57]  # inteiros
print(numeros)

alunos = ["Ana", "Bela", "Caio", "Diana"] # texto
            #0     #1      #2       #3
print(alunos)

# aceita qualquer tipo de dado
produto = ["Garrafa Térmica",  8,  49.55] # misturado
                  #0          #1   #2
print(produto)

# imprimir uma posição da lista
print(produto[0])
print(alunos[2])

print("Nome:", alunos[3])

print(f"Qtd: {produto[1]} / Preço: R$ {produto[2]}")


# alterar o conteúdo de uma posição da lista
# mudar o preço do produto
produto[2] = 34.99
print(produto)

alunos[3] = "Daiana"
print(alunos)


# só pode atualizar posições que existem na lista
alunos[9] = "Fabiano"   # erro (IndexError)







