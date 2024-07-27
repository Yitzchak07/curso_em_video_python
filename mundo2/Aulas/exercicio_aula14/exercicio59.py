menu = True
while menu == True:
    n1 = int(input('digite um numero:'))
    n2 = int(input('digite outro numero:'))

    print("[1]Somar")
    print("[2]multiplicar")
    print("[3]maior")
    print("[4]novos numeros")
    print("[5]Sair do programa")
    lista = int(input('digite a operacao:'))


    soma = n1 + n2
    multi = n1 * n2
    maior = n1 < n2
    if lista == 1:
        print(soma)
        break
    elif lista == 2:
        print(multi)
    elif lista == 3:
        if n1 > n2:
           maior = n1
        else:
           maior = n2
           print("o maior e {}".format(maior))
    elif lista == 4:
        menu == False
    elif lista == 5:
        print('saindo do programa')
        break
    
print("voce saiu")
        


    
