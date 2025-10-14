'''2. Crie um programa que use um laço
for e realize a soma dos números pares de 2 até 20. 
Exiba o resultado da soma.'''

soma = 0

for num in range(2,21,2): # 2 4 6 8 10 12 14 16 18 20
    soma += num

else:
    print("A soma é:", soma)
    