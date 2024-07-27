numero = True
soma = 0
cont = 0
while numero == True:
    n1 = int(input('digite um numero:'))

    if n1 == 999 :
       print("acabou")
       break
    elif n1:
        soma += n1
        cont += 1
    

print("{} numero foram digitado e soma de todos e {}".format(cont,soma))