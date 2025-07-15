'''1. Imprima os números de 1 a 50. Para cada número, se for múltiplo de 3,
imprima, na frente do número, a frase "MULTI-3". Se for múltiplo de 5,
imprima "MULTI-5". Se for múltiplo de ambos (3 e 5), imprima "MULTI-3-E-5”.
Se não for múltiplo nem de 3, nem de 5, imprima apenas o número.'''

num = 1

while num <= 50 :
    
    if num % 3== 0 and num % 5 == 0 :
        print(num, "MULTI-3-E-5")
    
    elif num % 3 == 0 :
        print(num, "MULTI-3")
    
    elif num % 5 == 0 :
        print(num, "MULTI-5")
    
    else:
        print(num)
        
    num = num + 1
    

