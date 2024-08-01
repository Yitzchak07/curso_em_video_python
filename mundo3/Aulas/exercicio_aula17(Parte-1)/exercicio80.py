lista = []
for c in range(0,5):

    n1 = int(input('digite um valor:'))

    if c == 0:
        lista.append(n1)
        print("adicionado no final da lista")
    elif n1 > lista[-1]:
        lista.append(n1)
    else:
        pos = 0
        while pos < len(lista):
            if n1 <= lista[pos]:
                lista.insert(pos, n1)
                print(f"adicionado na posicao {pos} da lista")
                break
            pos += 1

print(f"Os valores digitados em odem foram {lista}")

        
