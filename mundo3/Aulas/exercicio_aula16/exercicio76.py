produtos = ('lapis',1.75,'borracha',2.00,'caderno',15.90,'estojo',25.00,'trasfiridor',4.20,'compasso',9.99,'mochila',120.00,'canetas',22.30,'livro',34.90)

print("-"*20)
print("LISTAGEM DE PRECO")
print("-"*20)
print(len(produtos))

print(f"{produtos[0]}..........R$ {produtos[1]:.2f}")
print(f"{produtos[2]}..........R$ {produtos[3]:.2f}")
print(f"{produtos[4]}..........R$ {produtos[5]:.2f}")
print(f"{produtos[6]}..........R$ {produtos[7]:.2f}")
print(f"{produtos[8]}..........R$ {produtos[9]:.2f}")
print(f"{produtos[10]}.........R$ {produtos[11]:.2f}")
print(f"{produtos[12]}.........R$ {produtos[13]:.2f}")
print(f"{produtos[14]}.........R$ {produtos[15]:.2f}")
print(f"{produtos[16]}.........R$ {produtos[17]:.2f}")
print("-"*20)

# codigo do video!
print("=" * 30)
print(f"{"LISTAGEM DE PRECO":^30}")
print("=" * 30)
for pos in range(0,len(produtos)):
    if pos % 2 == 0:
        print(f'{produtos[pos]:.<30}',end='')
    if pos % 2 == 1:
        print(f"R${produtos[pos]:>7.2f}")
