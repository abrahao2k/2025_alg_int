'''10) Escreva um programa que o usuário informa o valor do salário
e o programa calcula o novo salário de acordo com as seguintes
condições:

Até R$ 1000,00 - 15%
Até R$ 2000,00 - 10%
Até R$ 3000,00 - 5%
Acima de R$ 3000,00 - 2.5%
'''

salario = float(input("Salário atual: "))

if salario <= 1000 :
    print(f"Novo salário = R$ {salario + (salario * 15/100) }")

elif salario <= 2000 :
    print(f"Novo salário = R$ {salario + (salario * 10/100) }")

elif salario <= 3000 :
    print(f"Novo salário = R$ {salario + (salario * 5/100) }")

else:
    print(f"Novo salário = R$ {salario + (salario * 2.5/100) }")
