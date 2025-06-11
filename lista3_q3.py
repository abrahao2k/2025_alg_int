'''3) Efetuar a leitura de três valores (variáveis A, B e C)
e apresentá-los dispostos em ordem crescente.'''

# abc  acb  bac  bca  cab  cba

a = int(input("Valor de A: "))
b = int(input("Valor de B: "))
c = int(input("Valor de C: "))

if   a < b < c : print(a, b, c)
elif a < c < b : print(a, c, b)
elif b < a < c : print(b, a, c)
elif b < c < a : print(b, c, a)
elif c < a < b : print(c, a, b)
else           : print(c, b, a)

#lista = [a,b,c]
#print(sorted(lista))