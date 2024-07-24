from random import randint
from time import sleep
computador = randint(0,5)# faz o compuador "PENSAR"
print("-=-"*20)
print("eu computador vou pensar em um numero!")
print("-=-"*20)
jogador = int(input("digite um numero entre (0) e (5) para descobrir qual o computador pessou:"))# jogador tenta adivinhar
print("PROCESSANDO... HUMMMM")
sleep(3)
if computador == jogador:# condicionais
    print("Ora voce ganhou de min pois eu pensei no numero {} e voce tambem pensou no numero {} 'PARABENS!'".format(computador,jogador))
else:
    print("voce perdeu eu pensei no numero {} e voce no {} HAHAHAHA Voce Perdeu".format(computador,jogador))