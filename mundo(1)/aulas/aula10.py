# estrutura condicional ou condicao

#se carro.esquerda: if carro.esquerda:
#senao carro.direira: else carro.direita:

#tempo = int(input('quantos anos tem seu carro?:'))
# print("carro novo"if tempo <=3 else"carro velho")
"""
nome = str(input('digite seu nome:')).strip().capitalize()
if nome == 'Isac':
    print("ola {} tudo bem legal ver voce aqui!".format(nome))

print('ola tudo bem {}'.format(nome))
"""
n1 = float(input('digite sua primeira nota:'))
n2 = float(input('digite sua segunda nota:'))
m = (n1 + n2) / 2
print("sua 1 nota e {} e a sua 2 e {} e sua media e {}".format(n1,n2,m))

if m >= 7.0:
    print("voce passou com sucesso, PARABENS!")
if m == 6.0:
    print('estude mais, mas parabens voce passou!')

if m >=4:
    print("voce esta de recuperacao, estude mais")
else:
    print("voce infelizmente reprovou mas ano que vem voce passa")