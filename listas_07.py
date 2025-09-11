# remover após uma pesquisa, evita erro

frutas = ["Morango","Cajá", "Banana", "Kiwi", "Melão", "Goiaba"]

pesquisa = input("Qual fruta quer remover? ")

if pesquisa in frutas :
    frutas.remove(pesquisa)
    print("Removido com sucesso.")
    print(frutas)

else:
    print("Não achei essa fruta na lista.")
