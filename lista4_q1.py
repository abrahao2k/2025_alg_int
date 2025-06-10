'''41. Solicite ao usuário que digite o valor do salário. Solicite a digitação
de cada uma das despesas a seguir: moradia, alimentação, transporte, lazer.
Calcule e mostre o saldo mensal (salário – despesas). Informe ao usuário se
ele está economizando ou se está gastando mais do que ganha.'''

salario = float(input("Digite o salário: "))

moradia = float(input("Despesa com moradia: "))
aliment = float(input("Despesa com alimentação: "))
transp  = float(input("Despesa com transporte: "))
lazer   = float(input("Despesa com lazer: "))

saldo = salario - (moradia + aliment + transp + lazer)
print("Saldo do mês: R$ ", saldo)

if saldo >= 0 :
    print("Está dentro do orçamento. Parabéns!")
else:
    print("Gastou mais do que ganha. Cuidado!")