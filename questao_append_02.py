'''Exercício 2: Média de Notas
Crie um programa que permita ao usuário inserir suas notas
(em valores reais) em uma lista usando um loop "while".
Quando o usuário inserir um valor negativo, o programa
deve parar de solicitar notas. Em seguida, calcule a média
das notas e exiba-a na tela.
'''

notas = []  # lista vazia

dig = 1
while dig >= 0 :
    dig = float(input("Digite a nota: "))
    
    if dig >= 0 :
        notas.append(dig) # adiciona na lista
else:
    soma = sum(notas)  # função sum soma os valores da lista
    qtd  = len(notas)  # função len conta os itens da lista
    media = soma/qtd
    print("A média das notas é: ", media) # sum(notas)/len(notas)

