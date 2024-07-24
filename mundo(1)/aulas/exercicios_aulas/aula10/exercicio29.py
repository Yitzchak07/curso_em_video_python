velocidade = float(input("qual e a velocidade atual do carro?:"))

if velocidade > 80:
    print("voce foi multado por esta em um velocidade acima da pertida que e 80km/h multa no valor ")
    multa = (velocidade-80) * 7
    print("valor da multa R${:.02f}".format(multa))

print("Tenha uma otima viajem, dirija com seguranca!")