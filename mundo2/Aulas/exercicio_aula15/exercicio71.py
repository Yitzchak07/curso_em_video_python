print("-" * 30)
print("{:.^30}".format("Caixa Eletronico 24HRS"))
print("-" * 30)

valor = int(input('Informe o valor que deseja sacar em R$ '))

total = valor
ced = 50
total_ced = 0
while True:
    if total >= ced:
        total -= ced
        total_ced += 1
    else:
        if total_ced > 0:
            print(f"total de {total_ced} cedulas de R${ced}")
        if ced == 50:
            ced = 20

        elif ced == 20:
            ced = 10

        elif ced == 10:
            ced = 1

        total_ced = 0
        if total == 0:
            break
print("="*30)
print("VOLTE SEMPRE AO BANCO")