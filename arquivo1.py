# INDICAR (ABRIR) O ARQUIVO A SER USADO

arquivo = open("novo.txt","w")   # w - modo gravação (write)

print("Arquivo aberto para gravação.")

arquivo.write("Meu primeiro arquivo salvo. :)\n")  # write grava txt no arq
arquivo.write("Esta é a segunda linha.")

arquivo.close()  # fechar arquivo após o uso

