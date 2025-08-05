import time
# LAÇO ENCADEADO (WHILE DENTRO DE WHILE)

linha = 1
while linha <= 3 :
    
    coluna = 1
    while coluna <= 3:
        print(f"Estou na linha {linha}, coluna {coluna}.")
        time.sleep(3) # pausa 3 segundos
        coluna += 1
    ## fim-while-coluna ##
    
    linha += 1
## fim-while-linha ##
    