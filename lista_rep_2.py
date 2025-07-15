'''2. Peça ao usuário para digitar uma senha. Se a senha for "python123",
o programa deve exibir "Senha correta!" e parar. Caso contrário, deve exibir
"Senha incorreta. Tente novamente." e continuar pedindo a senha. Use um laço
infinito e o comando break.'''

import getpass    # CTRL + T para executar no terminal do sistema

while True:
    
    #senha = input("Digite a senha: ")
    senha = getpass.getpass("Digite a senha: ")
    
    if senha == "python123" :
        print("Senha correta!")
        break
    else:
        print("Senha incorreta. Tente novamente.")
    
    