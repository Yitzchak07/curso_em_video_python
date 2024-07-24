a = int(input('digite o primeiro valor:'))
b = int(input('digite o segundo valor:'))
c = int(input('digite o terceiro valor:'))
# quem e o menor
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
# quem e o maior

maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print("o maior e o valor {}".format(maior))
print("o menor valor e {}".format(menor))