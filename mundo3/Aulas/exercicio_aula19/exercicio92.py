from datetime import datetime
pessoa = {'nome':'',"idade":'','carteira_de_trabalho':'','ano_contratacao':'','Salario':''}
pessoa['nome'] = str(input('digite seu nome:')).strip()
nasc = int(input(f"ano nascimento de {pessoa['nome']}:"))
pessoa["idade"] = idade = datetime.now().year - nasc

while True:
    pessoa['carteira_de_trabalho'] = int(input('Carteira de trabalho (0 Nao Tem):'))
    if pessoa['carteira_de_trabalho'] == 0:
        print(f"o nome e {pessoa['nome']}")
        print(f"a idade e {pessoa['idade']}")
        print(f"ctps {pessoa['carteira_de_trabalho']}")
        break
    else:
        pessoa['ano_contratacao'] = int(input('ano da contratacao:'))
        pessoa['Salario'] = float(input("Salario:R$"))
        pessoa["aposentadoria"] = ((pessoa['ano_contratacao'] + 35) - datetime.now().year)

        print(pessoa)
        print(f"o nome e {pessoa['nome']}")
        print(f"a idade e {pessoa['idade']}")
        print(f"ctps tem o valor {pessoa['carteira_de_trabalho']}")
        print(f"contratacao tem o valor {pessoa['ano_contratacao']}")
        print(f"salario tem o valor {pessoa['Salario']}")
        print(f"aposentaria e com {pessoa['aposentadoria']}")
        break
for k,v in pessoa.items():
    print(f'{k} tem o valor {v}')
    
