totalmil = total = cont = 0
menor = 0
while True:
    nome_produto = str(input("digite o nome do produto:"))
    preco = float(input("digite o preco do Produto R$:"))
    cont += 1
    total += preco
    
    if preco > 1000:
         totalmil += 1
    if cont == 1:
        menor = preco
    else:
        if preco < menor:
            menor = preco

    sair = " "
    while sair not in "SN":
        sair = str(input("deseja continuar? [S/N]:")).upper().strip()[0]
    if sair == "N":
        break
            
print(f"total de Gastos R${total}")
print(f"total de produtos mais de R$1000.00 e {totalmil}")
print(f"O nome do menor produto e R${menor:.2f}")