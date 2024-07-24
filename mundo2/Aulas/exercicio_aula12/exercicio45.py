import random
from time import sleep
print("computador malvado:voce aqui dnv vamos jogar jokenpo escolha entre (pedra) ou (papel) ou(tesoura) dessa vez voce perde hahaha")
print("1")
jogador = str(input("escolha para se salvar nao deixe o computador ganhar:")).strip()
print("Computador Malvado: Eu Escolho hmmmmmm!")
sleep(1.2)

computador = random.choice(["pedra","papel","tesoura"])

if computador == "tesoura" and jogador == "papel":
    print("voce perdeu pois eu esolhi {} e voce {}".format(computador,jogador))

elif computador == "pedra" and jogador == "tesoura":
    print("voce perdeu eu escolhi {} e voce {}".format(computador,jogador))

elif computador == "papel" and jogador == "pedra":
    print("voce perdeu eu escolhi {} e voce {} hahahaha".format(computador,jogador))
elif computador == jogador:
    print("Eu e Voce escolhemos a mesma coisa, vamos dnv voce {} e eu {}".format(jogador,computador))
else:
    print("Voce Ganhou Pois voce escolheu {} e Eu {}, MAS SAIBA QUE NAO AVERA PROXIMA VEZ HAHAHAHAHA".format(jogador,computador))
