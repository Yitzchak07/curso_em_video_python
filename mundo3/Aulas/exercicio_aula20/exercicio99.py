def maior(*nun):
    cont = maior = 0
    print('\nanalisando os valores passados')
    for valor in nun:
        print(f"{valor}",end=" ", flush=True)
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print(f"foram informado {cont} valores ao todo")
    print(f"o maior valor e {maior}")
maior(2,9,4,5,7,1)
maior(4,7,0)
maior(1,2)
maior(6)
maior()
