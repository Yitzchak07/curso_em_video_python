print("10 TERMOS DE UMA PÁ")
primeiro = int(input("primeiro termo:"))
razao = int(input("razao da pá:"))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print("-> {}".format(termo),end=" ")
        termo += razao
        cont += 1
    print("\nPausa")
    mais = int(input("mais quantos termos voce que adicionar:"))
print("Fim")