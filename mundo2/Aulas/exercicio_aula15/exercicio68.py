from random import randint
print("VAMOS JOGAR PAR OU IMPAR")
vitoria = 0
while  True:
    computador = randint(1,10)
    jogador = int(input('diga um valor:'))
    total = jogador + computador
    tipo = " " 
    while tipo not in 'PpiI':
        tipo = str(input('Voce quer [Par] ou [Impar]?:')).capitalize().strip()[0]
    print(f"voce jogou {jogador} e o computador {computador} o total e {total}", end=" ")
    print(" DEU PAR "if total % 2 == 0 else "DEU IMPAR")
    if tipo == "P":
        if total % 2 == 0:
            print("voce ganhou")
            vitoria += 1
        else:
            print("voce Perdeu")
            break
    if tipo == "I":
        if total % 2 == 1:
            print("voce ganhou!")
            vitoria += 1
        else:
            print("voce Perdeu!")
            break
    print("vamos jogar novamente!")
print(f"Gamer Over! Voce venceu {vitoria} ")