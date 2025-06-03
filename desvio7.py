import getpass    #pwinput
# REALIZAR O LOGIN DE UM USUÁRIO

usuario = input("Digite o usuário: ")
senha   = getpass.getpass("Digite a senha: ")

# AND - só entra no if se TODAS AS COMPARAÇÕES forem verdadeiras

if usuario == "admin" and senha == "1234" :
    print("ACESSO PERMITIDO!")
else:
    print("ACESSO NEGADO!")

