n1 = (int(input('digite um numero:')),
      int(input('digite outro numero:')),
      int(input('digite mais outro numero:')),
      int(input('digite agora o ultimo numero:')))
print(f"Voce digitou os Numeros {n1}")
print(f"O numero 9 aparece {n1.count(9)} vezes")
if 3 in n1:
    print(f"o valor 3 apareceu na {n1.index(3)+1} posicao")
else:
    print("o valor 3 apareceu em nenhuma posicao!")
print("Os valores pares digitados foram ",end="")

for n in n1:
    if n % 2 == 0:
        print(n,end=" ")
    
