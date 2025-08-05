# LAÇO INFINITO

while True: #laço infinito
    
    op = input("Menu\n1-Digitar\n2-Imprimir\n3-Sair\nOpção? ")
    
    if op == "1" :
        nome = input("Qual o seu nome?")
        print(f"Olá, {nome}!")
              
    if op == "2" :
        print("Essa é uma frase padrão do sistema.")
    
    if op == "3" :
        break  # finaliza o laço, mesmo infinito
    