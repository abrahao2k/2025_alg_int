# ELIF

n1 = int(input("Valor 1: "))
n2 = int(input("Valor 2: "))
print("ESCOLHA A OPERAÇÃO:\n 1-Soma\n 2-Subtr\n 3-Mult\n 4-Div")
op = int(input("Opção? "))
         
if op == 1:
    print(n1+n2)
elif op == 2 :
    print(n1-n2)
elif op == 3 :
    print(n1*n2)
elif op == 4 :
    print(n1/n2)
else:
    print("Opção inválida.")


    