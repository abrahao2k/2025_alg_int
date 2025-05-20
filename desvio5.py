# pergunte em qual escola o aluno estuda. se for IFRN diz que é
# a melhor escola. se for outra, diz que não.

escola = input("Em qual escola você estuda? ")

if escola.upper() == "IFRN" :         # upper() transforma em maiúsculas
    print("Essa escola é a melhor!")

else:
    print("Essa escola ainda pode melhorar.")



