soma = cont = 0
print("para interroper o programa digite 999")
while True:
    numero = int(input('digite um numero:'))

    if numero == 999:
        break
    soma += numero
    cont += 1
print(f"Numeros digitados {cont} a soma de todos os {cont} e {soma}")