# while - else

resposta = "sim"

while resposta == "sim" :
    resposta = input("Você gosta de açaí? (sim/nao) ")
    print(" :) ")
    #break
    
else:
    print("Não sabe o que está perdendo...")

# o else será executado quando a comparação do while for falsa
# se o comando break for executado, não passa no else