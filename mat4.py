# CONVERSOR DE MOEDA
# Crie um programa que pergunta o valor da cotação do dólar,
# depois pergunta quanto em Reais o usuário tem.
# Calcule quantos dólares valem o dinheiro do usuário.

cotacao = float(input("Cotação do Dólar: ")) # float - casas decimais
dinheiro = float(input("Valor em Reais: "))

dolares = dinheiro / cotacao

print(f"R$ {dinheiro:.2f} valem US$ {dolares:.2f}") # :.2f - 2 casas decimais

