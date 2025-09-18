# INSERIR EM OUTRA POSIÇÃO
lista = ["Azul","Verde","Marrom","Branco"]
           #0       1      2         3

lista.insert(2,"Lilás")
print(lista)

# se usar uma posição que não existe, vai pro fim da lista
lista.insert(10,"Vermelho")
print(lista)