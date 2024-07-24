from time import sleep

inicio = str(input('digite para iniciar!:'))
for cont in range(10,-1,-1):
    
    print("falta {} segundos para a queimas de fogos".format(cont))
    sleep(1)
    if cont == 0:
        print("QUEIMAS DE FOGOS! BOOOOMMMM ")