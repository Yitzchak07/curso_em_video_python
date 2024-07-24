salario = float(input('digite seu salario para saber seu aumento:'))



if salario <= 1250:
    novo = salario + (salario * 15/100)
    print('voce recebeu um auemto salarial de (10%) novo salario {:.02f}'.format(novo))

else:
    novo = salario + (salario * 10/100)
    print('voce recebeu um aumento salarial de (15%) seu salario agora e {:.2f}'.format(novo))