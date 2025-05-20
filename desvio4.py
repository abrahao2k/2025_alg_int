# pergunte a idade do usuário e diz se ele pode ou não votar (16+)

idade = int(input("Digite a idade: "))

if idade >= 16 :
    print("Você já pode votar.")
    print("Escolha com sabedoria.")

else:
    print("Você ainda não pode votar.")
    print("Em breve poderá.")


print("Fim.")
