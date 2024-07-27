from random import randint
from time import sleep 
print("Voce Sentiu Uma Presencao Misteriosa!")
sleep(1)
print("-="*10)
print("I AM: Voce Aqui Denovo Vamos Jogar Um Jogo Hahahah!")
print("-="*10)
computador = randint(0,10)
errou = -1

while computador == computador:
    acerte = int(input('digite o numero que o I AM pensou:'))
    print(computador)
    if acerte == computador:
        errou += 1
        print("Voce Conseguiu HAhaha")
           
        break
    elif computador != acerte:
        print("tente dnv")
        errou += 1
        if acerte > computador:
            print("o numero que voce digitou e maior")
        else:
            print("o numero que voce digitou e menor")
    
print("voce errou {} vezes que vergonha! hahahaha".format(errou))
    
