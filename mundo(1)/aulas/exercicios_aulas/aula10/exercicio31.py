from time import sleep
viagem = float(input('digite a distancia da viagem:'))
print("processandor viagem!")
sleep(1.5)
print("voce esta prestes a comecar uma viagem de {}km.".format(viagem))
if viagem <= 200:
    preco = (viagem * 0.50)
    
else:
    preco = (viagem * 0.45)
print("o preco da sua viagem sera de R${:.2f}".format(preco))
    