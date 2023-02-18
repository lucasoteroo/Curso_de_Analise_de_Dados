par=0
for i in range(5):
    numero= int(input("digite um número inteiro: "))
    if (numero%2 == 0 ):
        par+=1
if par==1:
    print("Tem",par,"número par dentre os que você inseriu")
else:
    print("Tem",par,"números pares dentre os que você inseriu")
