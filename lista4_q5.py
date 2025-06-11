'''45. Escreva um programa que verifica se um usuário pode entrar
em um evento que está acontecendo em um clube. Peça ao usuário
para inserir sua idade e se ele tem convite (sim ou não). Se a
idade for 18 ou mais e tiver convite, exiba "Entrada permitida".
Caso contrário, exiba "Entrada negada".'''

idade = int(input("Digite a idade: "))
convite = input("Possui convite? (sim/não) ")

if idade >= 18 and convite == "sim" :
    print("Entrada permitida!")

else:
    print("Entrada negada.")

