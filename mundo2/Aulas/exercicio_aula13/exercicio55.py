maior = 0
menor = 0
for pessoa in range(1,6):
    peso = float(input('peso da {}a pessoa:'.format(pessoa)))

    if pessoa == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso

print("o maior peso foi kg{}".format(maior))
print("o menor peso foi kg{}".format(menor))