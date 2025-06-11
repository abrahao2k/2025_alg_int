'''46. Escreva um programa que peça ao usuário para inserir
a temperatura (em graus Celsius) e se está chovendo (sim ou não).
Se a temperatura for menor que 15 e estiver chovendo,
exiba "Está frio e chuvoso". Se a temperatura for menor que 15
e não estiver chovendo, exiba "Está frio". Se a temperatura for
15 ou mais e estiver chovendo, exiba "Está quente e
chuvoso". Caso contrário, exiba "Está quente".'''

temp = float(input("Digite a temperatura: "))
chuva = input("Está chovendo? (sim/nao) ")

if temp < 15 :
    if chuva == "sim" :
        print("Está frio e chuvoso")
    else:
        print("Está frio")

else: # 15 ou +
    if chuva == "sim":
        print("Está quente e chuvoso")
    else:
        print("Está quente")
        


