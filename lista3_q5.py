'''5) Escreva um programa que informa sobre a aprovação de um
empréstimo habitacional. O usuário informa o valor da casa, o
salário e a quantidade de anos a pagar. O valor da prestação
não pode ser superior a 30% do salário. Informe o valor da
prestação e se o empréstimo será aprovado ou não. Não são
considerados juros neste exemplo.'''

valor_casa = float(input("Valor da casa: "))
salario    = float(input("Salário: "))
anos       = float(input("Anos para pagamento: "))

prestacao  = valor_casa / (anos * 12)
print(f"Prestação = R$ {prestacao:.2f}")

margem     = salario * 30/100
print(f"Margem = R$ {margem:.2f}")

if prestacao <= margem :
    print("Empréstimo aprovado.")
else:
    print("Empréstimo negado.")


