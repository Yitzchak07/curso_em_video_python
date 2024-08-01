lista = []
while True:
    
    n1 = int(input('digite um numero:'))

    if n1 not in lista:
        lista.append(n1)
        print("valor adicionado com sucesso!")
    else:
        print("numero repetido nao vai ser adicionado")



    sair = " "
    sair = str(input('quer continuar?[S/N]:')).upper().strip()
    if sair == "N":
        print("voce saiu")
        break

print(f"valor digitados {lista}")