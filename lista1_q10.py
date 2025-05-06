'''10) O cardápio de uma lanchonete é dado abaixo.
Prepare um algoritmo que leia a quantidade de cada item que você 
consumiu e calcule a conta final. 
Hambúrguer................. R$  8,00 
Cheeseburger............... R$ 10,00 
Fritas..................... R$  6,00 
Refrigerante............... R$  5,00 
Milkshake.................. R$ 12,00 '''

q1 = int( input("Qtd. Hambúrguer? ") )
q2 = int( input("Qtd. Cheeseburger? ") )
q3 = int( input("Qtd. Fritas? ") )
q4 = int( input("Qtd. Refrigerante? ") )
q5 = int( input("Qtd. Milkshake? ") )

total = q1*8.00 + q2*10.00 + q3*6.00 + q4*5.00 + q5*12.00

print(f"Total da conta = R$ {total:.2f}")