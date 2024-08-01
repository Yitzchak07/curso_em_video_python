from random import randint
maior = menor = 0
sorteio = (randint(1,10),randint(1,10),randint(1,10),randint(1,10),randint(1,10))
print(f'os numeros sorteados foram {sorteio}')

print(f"o maior numero e {max(sorteio)}")
print(f"o menor numero foi {min(sorteio)}")