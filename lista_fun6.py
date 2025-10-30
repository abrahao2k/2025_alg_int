# 6.Crie uma função que recebe um número e diz se ele é primo.
def primo(num):
    if num <= 1 :
        print("NÃO É PRIMO")
    elif num == 2 :
        print("É PRIMO")
    elif num % 2 == 0 :
        print("NÃO É PRIMO")
    
    else:
        achou_divisor = False
        for x in range(3, int(num**0.5) + 1, 2) :
            if num % x == 0:
                print("NÃO É PRIMO")
                achou_divisor = True
                break
        
        if achou_divisor == False:
            print("É PRIMO")
    
primo(97)    