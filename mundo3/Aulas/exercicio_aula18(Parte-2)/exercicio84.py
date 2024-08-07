temp = []
princ = []
maior = menor = 0

while True:

    temp.append(str(input('nome:')).strip())
    temp.append(float(input('seu peso:')))
    if len(princ) == 0:
        maior = menor = temp[1]
    else:
        if temp[1] > maior:
            maior = temp[1]
        if temp[1] < menor:
            menor = temp[1]
    princ.append(temp[:])
    temp.clear()

    resp = str(input('deseja continuar[S/N]:')).strip().upper()
    
    



    if resp == "N":
        break
print(f"total de pessoas cadastradas {len(princ)}")
print(f"o maior peso foi de {maior}Kg")
print(f"o menor peso foi {menor}Kg")