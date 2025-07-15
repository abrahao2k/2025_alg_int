'''3. Faça um programa que usa um laço para escrever os números de 1 a 100,
excluindo (pulando) os múltiplos de 4. Use o comando continue.'''

num = 0

while num < 100 :
    
    num = num + 1
    
    if num % 4 == 0 : continue
    
    print(num)
    