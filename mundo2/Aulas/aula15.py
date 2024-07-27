# lacos rpeticao parte 3

'''
while True:
    bloco = 'caminho'
    buraco = 'buraco'
    moeda = 'moeda'
    trofel = 'trofel'
    
    if bloco:
        passo = bloco = 'andar'
    if buraco:
        pular = buraco = 'pular buraco'
    if moeda:
        pegar_moeda = moeda = 'pegou a moeda'
    if trofel:
        pular
    break
pegar = "pegou"
'''
cont = soma = 0 
while True:
    nu = int(input('digite um numero:'))
    cont += 1
    if nu == 999:
        break
    soma += nu
print('acabou')
print("soma de todos os valores e {}".format(soma))
print(f"a soma vale {soma}")