lista = []
cont = 0
while True:
    lista.append(int(input('digite um numero:')))
    print(lista)
    cont += 1

    sair = "S"
    sair = str(input('deseja sair [S/N]')).upper().strip()
    if sair == "S":
        print('voce saiu')
        break
print(lista)
print(f"total de numero digitados {cont}")
lista.sort(reverse=True)
print(f"Lista em valores decrescente {lista}")
if 5 in lista:
    print(f"o valor 5 Faz Parte da Lista")
    print(lista)
else:
    print("o valor 5 Nao Faz Parte da Lista!")