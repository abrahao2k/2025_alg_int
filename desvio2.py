# PERGUNTE A IDADE DO USUÁRIO
# MOSTRE UMA MENSAGEM DE ACORDO COM A TABELA ABAIXO
# DE 1 A 11 ANOS  - VOCÊ É CRIANÇA
# DE 12 A 17 ANOS - VOCÊ É ADOLESCENTE
# 18 ANOS OU MAIS - VOCÊ É ADULTO

idade = int(input("Digite a idade: "))

if 1 <= idade <= 11 :
    print("Você é criança.")

if 12 <= idade <= 17 :
    print("Você é adolescente.")

if idade >= 18 :
    print("Você é adulto.")