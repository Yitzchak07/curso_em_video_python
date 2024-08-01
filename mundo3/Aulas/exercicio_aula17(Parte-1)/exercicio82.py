lista = []
par = list()
impar = list()
while True:
    

    lista.append(int(input('digite um valor:')))
    
    sair = str(input('deseja sair [S/N]:')).upper().strip()

    if sair == "S":
        print("voce saiu")
        break
for i, v in enumerate(lista):
    if v % 2 == 0:
        par.append(v)
    elif v % 2 == 1:
        impar.append(v)

print(f"A lista {lista}")
print(f"lista de numeros pares {par}")
print(f"lista de numeros impares {impar}")


    