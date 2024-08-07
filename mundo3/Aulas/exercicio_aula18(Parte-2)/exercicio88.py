from random import randint
lista = list()
jogos = list()
cont = 0
quant = int(input('quantos jogos voce quer quue eu sorteie?:'))
tot = 0
while tot <= quant:
    cont = 0
    while True:
        nun = randint(1,60)
        if nun not in lista:
            lista.append(nun)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
print(f"os numeros sorteados foram {jogos}",end="")
for i, l in enumerate(jogos):
    print(f'jogos {i}:{l}')
