'''4. Peça ao usuário para digitar um número inteiro de linhas. Crie um padrão
de asteriscos onde a primeira linha tem 1 asterisco, a segunda tem 2, e assim
por diante, até a quantidade de linhas. Use laços encadeados.
Exemplo (para linhas = 4):
*
**
***
****
'''

linhas = int(input("Digite o número de linhas: "))

linha_atual = 1

while linha_atual <= linhas :
    
    coluna = 1
    while coluna <= linha_atual :
        print("*", end=" ")    # não pula linha, põe espaço no final
        coluna += 1
    
    print("")  # pula pra próxima linha
    linha_atual += 1  # incremento (passa pra próxima linha)
    
    
    
    
    
    
    