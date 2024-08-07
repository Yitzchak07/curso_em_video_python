# Dicionarios!
# dados = dict()
dados = {'nome':"Isac",'idade':17}
print(dados['idade'])# idade 17
print(dados['nome'])# nome Isac
dados['sexo'] = "M"# adicionar novos elementos ao dicionario!
print(dados['sexo'])
print(dados)
#del dados['idade']# eliminar elemento do dicionario!


print(dados)
filmes = {'titulos':'transformes',
          'ano': 2018,

}
print(filmes.values())# vai retornar todos os valores do dicionario!
print(filmes.keys())# chaves do dicionario = titulos e ano 
print(filmes.items())# vai pegar o valores e chaves do dicionario = titulo transformes ano 2018!
for k,v in filmes.items():# para cada chave e valor no filme.items 
    print(f"o {k} e {v}")
dados['peso'] = 85.9
for k,v in dados.items():
    print(f"{k} = {v}")
# brasil = []
# estado1 = {'Uf':"Goias",'sigla':"GO"}
# estado2 = {'Uf':"Bahia",'sigla':"BA"}
# brasil.append(estado1)
# brasil.append(estado2)
# print(brasil[0]['sigla'])

estado = dict()
brasil = list()

for c in range(0,3):
    estado['Uf'] = str(input('digite o nome do estado que deseja adicionar:')).strip().capitalize()
    estado['sigla'] = str(input('digite a sigla do estado:')).strip().capitalize()
    brasil.append(estado.copy())
for e in brasil:
    for k,v in e.items():
        print(f"o campo {k} tem o valor {v}")
