# COMANDO BREAK - FINALIZA IMEDIATAMENTE O LAÇO

while True:
    resposta = input("Você quer sair do laço? (s/n) ")
    
    if resposta == "s" :
        break
    
    else:
        print("Tá bom, vou ficar repetindo aqui...")


## fora do laço #################################################
print("CHEGAMOS AO FIM!")