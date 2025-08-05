# PARTES DE UM LAÇO DE REPETIÇÃO

# 1. VARIÁVEL DE CONTROLE
resposta = "sim"

# 2. TESTE LÓGICO
while resposta == "sim" :
    nome = input("Qual é o seu nome? ")
    print(f"Seja bem vindo, {nome}.")
    
    # 3. INCREMENTO (mudança da variável de controle)
    resposta = input("Repetir? (sim/não) ")
    