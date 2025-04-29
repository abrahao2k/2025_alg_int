# DIGITAR VALORES DE UMA OPERAÇÃO
valor1 = int( input("Digite um valor: ") ) #converte para inteiro
valor2 = int( input("Digite outro valor: ") ) 

total = valor1 + valor2
print(f"Soma = {total}")

sub = valor1 - valor2
print(f"Subração = {sub}")

mult = valor1 * valor2
print(f"Multiplicação = {mult}")

div = valor1 / valor2
print(f"Divisão = {div:.2f}") #  :.2f  - formata a qtd casas decimais