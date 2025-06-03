# login de vários usuários

u = input("Usuário? ")
s = input("Senha? ")

if (u=="adm" and s=="123") or (u=="vend" and s=="456"):
    print("Acesso permitido.")

else:
    print("Acesso negado.")

