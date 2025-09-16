'''Exercício 1: Preenchimento de Lista
Escreva um programa que peça ao usuário para inserir números
inteiros positivos e os armazene em uma lista. O programa deve
continuar pedindo números até que o usuário insira um número
negativo. Em seguida, exiba a lista resultante.'''

numeros = list()   # lista vazia

digitado = 1
while digitado >= 0 :   # enquanto positivo
    digitado = int(input("Digite um número: "))
    
    if digitado >= 0:            #adiciona na lista se positivo
        numeros.append(digitado)
else:
    print("Números digitados:", numeros)
    