# DESVIO ENCADEADO NO ELSE

tempo = int(input("Tempo (minutos): "))
veiculo = input("Qual veículo (carro/moto): ")

if tempo <= 10 :
    print("Estacionamento GRÁTIS!")

else:  # passou de 10 min
    if veiculo.lower() == "moto" :
        print("Tarifa de Moto: R$ 5,00")
        
    else:
        print("Tarifa de Carro: R$ 10,00")

