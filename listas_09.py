# remover apenas posições existentes
frutas = ["Morango","Cajá", "Banana", "Kiwi", "Melão", "Goiaba"]

posicao = int(input("Qual posição remover? "))

if posicao < len(frutas) :
    frutas.pop(posicao)
    print("Removido.")
    print(frutas)

else:
    print("Posição inválida.")