'''Leia a hora inicial, minuto inicial, hora final e minuto final de um jogo. A seguir calcule a duração do jogo.'''
hrini= int(input("Digite a hora que o jogo iniciou: "))
minini= int(input("Digite os minutos que o jogo iniciou: "))

hrfim= int(input("Digite a hora que o jogo encerrou: "))
minfim= int(input("Digite os minutos que o jogo encerrou: "))

hrjogo=abs(hrfim)-(hrini)
minjogo= (minfim-minini)


if hrjogo !=24:
    if minjogo<0:
        hrjogo-=1
        minjogo+=60
        
    print("O JOGO DUROU ",hrjogo," HORA(S) E ",minjogo," MINUTO(S)")
else:
        print("O jogo excedeu o limite de horas")
