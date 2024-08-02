nun = [[],[]]
valor = 0
for c in range(1,8):
    valor = int(input('digite um valor:'))
    if valor % 2 == 0:
        nun[0].append(valor)
        
    else:
        nun[1].append(valor)     
    

print(f"todos os valor par {nun[0]}")
print(f'todos os valores impares {nun[1]}')

        