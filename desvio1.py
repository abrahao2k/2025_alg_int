temp = float(input("Temperatura: "))

if temp > 25 :
    print("Que calor!")
    print("Esfrie mais!")
    
if temp >= 18 :
    if temp <= 25 :
        print("Temperatura agradável!")
        print("Não mude.")
    
if temp < 18 :
    print("Que frio!")
    print("Esquente um pouco!")

print("FIM")