'''5. Crie um programa que simula um aplicativo bancário. Crie a variável saldo
iniciando com valor zero. Use um laço infinito para exibir o menu com as opções:
1 – Ver saldo, 2 – Depositar, 3 – Sacar, 4 – Sair.
Peça ao usuário para digitar a opção desejada. Use if/elif/else para testar a
opção digitada. Se digitar 1, imprime o saldo atual. Se digitar 2,
pergunta um valor e soma ao saldo atual. Se digitar 3, pergunta 
um valor, testa se há saldo disponível e subtrai do saldo; caso não
tenha saldo suficiente (saque > saldo), exibe a mensagem “Saldo insuficiente.”.
Se digitar 4, finaliza o laço com o comando break.'''

saldo = 0
while True:
    print('==MENU==\n 1-Saldo\n 2-Depositar\n 3-Sacar\n 4-Sair')
    op = int(input("Opção? "))
    
    if   op == 1 : print(f"O saldo é : R$ {saldo} \n")
    
    elif op == 2:
        valor = float(input("Digite o valor do depósito: "))
        saldo += valor
        print("Depósito efetuado \n")
    
    elif op == 3:
        valor = float(input("Digite o valor do saque: "))
        if valor <= saldo :
            saldo -= valor
            print("Saque realizado \n")
        else:
            print("Saldo insuficiente \n")
            
    else:
        break
    
    
    
    
    
    
    