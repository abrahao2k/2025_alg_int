'''42. Solicite a digitação da quantidade de itens a ser comprado e o valor
do item. O cliente receberá desconto de 5% se comprar mais de 10 itens ou
se o valor total da compra for acima de R$ 100,00. Informe o valor total e,
se ele ganhou desconto, quanto foi o desconto e quanto deverá pagar.'''

quant = float(input("Quantidade de itens: "))
valor = float(input("Valor unitário: "))

total = quant * valor
print("Valor total = R$", total)

if quant > 10  or  total > 100:
    print("Ganhou 5% de desconto :) ")
    
    desc = total * 5/100
    print("Desconto = R$", desc)
    
    pagar = total - desc
    print("Valor a pagar = R$", pagar)
    

