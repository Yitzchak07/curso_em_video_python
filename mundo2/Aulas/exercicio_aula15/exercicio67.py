while True:
    numero = int(input('Que ver a tabuada de qual valor?:'))
    if numero < 0:
        break
    for tabuada in range(1,11):
        print(f"A tabuada do {numero} e {numero} x {tabuada} = {numero*tabuada}")
    
print("programa tabuada encerrado!")
