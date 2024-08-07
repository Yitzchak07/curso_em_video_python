nota = {}
nota["nome"] = str(input('nome do aluno:')).strip().capitalize()
nota["media"] = float(input(f'qual e a Média de {nota["nome"]}:'))
print(f'o nome e igual a {nota["nome"]}')
print(f'Média e igual a {nota["media"]}')

if nota["media"] >= 6:
    print("situacao e igual a aprovado")
else:
    print("situacao e igual a reprovado")

