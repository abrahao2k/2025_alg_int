import io
try:
    arq = open("alunos.txt", "r") # r - read/leitura

    texto = arq.read()  # lê o conteudo e guarda na variável
    
    #arq.write("legal")
    
    print("ALUNOS CADASTRADOS")
    print(texto)

    arq.close()

except FileNotFoundError:
    print("Erro ao abrir o arquivo.")

except io.UnsupportedOperation:
    print("Gravação não suportada.")