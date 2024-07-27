print("10 TERMOS DE UMA PÁ")
primeiro = int(input("primeiro termo:"))
razao = int(input("razao da pá:"))
termo = primeiro
cont = 1
while cont <= 10:
    print("-> {}".format(termo),end=" ")
    termo += razao
    cont += 1
print("\nfim")