"""
faca um programa que leia o comprimento do cateto aposto
e do catedo adjacento de um triangulo retangulo, calcule
e mostre o comprimento da hipotenusa.

"""
co = float(input('çomprimento do cateto oposto: '))
ca = float(input('comprimento do cateto adjacento: '))

hi = (co ** 2 + ca ** 2) ** (1/2)
print("A hiportenusa vai medir {:.02f}".format(hi))

from math import hypot
opo = float(input("comprimento do cateto oposto:"))
ad = float(input("comprimento do cateto adjacento:"))
hip = hypot(opo,ad)
print(f"a hipotenusa vai medir {hip:.2f}")
