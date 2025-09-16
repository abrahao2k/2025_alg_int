'''Exercício 4: Números Pares
Crie um programa que preencha uma lista com números pares
automaticamente, usando um loop "while". A lista deve conter
os primeiros 10 números pares.
 Por fim, imprima a lista.'''

pares = []

num = 2
while num <= 20 :
    pares.append(num)
    num += 2

print(pares)
print("A soma é:", sum(pares))