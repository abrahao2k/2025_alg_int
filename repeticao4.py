import random
sorteado = random.randint(1,100)

digitado = 0  # qualquer número que NÃO esteja entre 1 e 100
tentativas = 0
while digitado != sorteado :
    
    digitado = int(input("Digite um número entre 1 e 100: "))
    tentativas = tentativas + 1
    if digitado == sorteado:
        print("PARABÉNS! VOCÊ ACERTOU!")
        print("TENTATIVAS = ", tentativas)
    elif digitado < sorteado :
        print("Tente um número MAIOR.")
    
    elif digitado > sorteado :
        print("Tente um número MENOR.")
    