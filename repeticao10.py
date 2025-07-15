# LAÇOS ENCADEADOS - WHILE DENTRO DE WHILE

while True:  ##### LAÇO PRINCIPAL QUE CONTROLA O MENU #####
    print("== MENU ==\n 1-Imprimir mensagem\n 2-Digitar 5 numeros\n 3-Sair")
    op = int(input("Opção? "))
    
    if op == 1 : print("Essa é sua mensagem especial. :) ")
    
    elif op == 2 :
        ######################## LAÇO INTERNO QUE CONTA AS REPETIÇÕES ####
        cont = 0
        while cont < 5 :
            num = input("Digite um número: ")
            print("Você digitou", num)
            cont += 1
        ##################################################################
            
    elif op == 3: break
    
print("FIM DO PROGRAMA")