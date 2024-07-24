#estrutura de repetiçao for laco com variavel de controle


'''
laco c no intervalo(1,10):
    passo
pegar
'''

c = 0
for c in range(1,10):
    passo = "passo"
    print(passo,c)
pega = "pegar"
print(pega,c)

'''
laco b no intervalo(0,3)
    passo 
    pula
passo
pega
'''
print("_"*10)
for a in range(0,110,10):
    print("oi",a)
    print("Ola Mundo",a)
print("Fim")

b = 0
print("_"*10)
for b in range(0,3):
    moeda = "moeda"
    if moeda:
        moeda = "pegou a moeda"
        print(moeda)
    
    passo
    pula = "pula"
    print(passo,b)
    print(pula,b)
print(passo,b)
print(pega,b)
"""
inicio = int(input('digite um numero:'))
fim = int(input("fim:"))
passou = int(input('passo:'))

for g in range(inicio,fim,passou):
    print("numero",g)
    
"""

v = 0
for n in range(1,3):
    n1 = int(input('digite um numero:'))
    v += n1
    print(v)
    
    
    