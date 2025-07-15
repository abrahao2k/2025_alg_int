# CONTINUE - REINICIA O LAÇO, MESMO SEM TER EXECUTADO TUDO
# Faça um programa que solicita a digitação de 5 números positivos
# Se o número for negativo, mostra uma mensagem e não conta
# como número válido

contador = 0

while contador < 5 :    # <--------------------------------
    numero = int(input("Digite um número positivo: "))  # |
                                                        # |
    if numero < 0 :                                     # |
        print("Esse número é negativo. Recusado.")      # |
        continue    # volta para o início do laço ---------
    
    print("Número aceito.")
    contador = contador + 1

print("Parabéns, você digitou 5 números positivos.")
                 
                 