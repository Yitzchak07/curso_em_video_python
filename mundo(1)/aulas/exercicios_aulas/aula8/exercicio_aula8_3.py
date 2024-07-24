from math import sin,cos,tan,radians
angulo = float(input('digite um algulo que voce deseja:'))
seno = sin(radians(angulo))
print('o angulo de {} tem o SENO de {:.2f}'.format(angulo,seno))
cosseno = cos(radians(angulo))
print("o angulo de {} tem o COSSENO de {:.2f}".format(angulo,cosseno))
tangeno = tan(radians(angulo))
print("o angulo de {} tem o tangeno de {:.2f}".format(angulo,tangeno))