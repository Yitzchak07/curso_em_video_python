sair = "N"
media = 0
soma = quant = media = maior = menor = 0

while sair in "N":
    numero = int(input("digite um numero:"))
    sair = str(input('desejs sair[S/N]:')).upper().strip()[0]
    soma += numero
    quant += 1
    if quant == 1:
        maior = menor = numero
    else:
        if numero > maior:
            maior = numero
        if numero < menor: 
            menor = numero
    
    
media = soma / quant
print("voce digitou {} numeros e a media foi {}".format(quant,media))
print("o maior numero foi {} e o menor foi {}".format(maior,menor))