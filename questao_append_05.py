'''Exercício 5: Contagem Regressiva
Escreva um programa que crie uma lista contendo números de
10 a 1 em ordem decrescente usando um loop "while".
Em seguida, exiba a lista resultante.'''

contagem = []
num = 10
while num >= 1 :
    contagem.append(num)
    num -= 1

print("Contagem regresiva:", contagem)