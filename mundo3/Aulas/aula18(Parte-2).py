# lista Parte 2

dados = []
dados.append("pedro")
dados.append(25)
print(len(dados))
print(dados)
print(dados[0])
print(f"nome {dados[0]} idade {dados[1]}")
pessoas = [['pedro',25],['maria',19],['joao',33]]# listas dentro de listas conceito dos exercicios da aula 18
dados[0] = 'isac'
dados[1] = 18
pessoas.append(dados[:])
print(pessoas)
#               0    1      0     1      0    1
#               0              1           3
print(pessoas[0])
print(pessoas[0][0])# pessoas 0 no item 0!
print(pessoas[1][1])
print(pessoas[1][0:])
print(pessoas[0][1])
galera = list()
info = list()
media = 0
for c in range(0,4):
    info.append(str(input('nome:')).strip())
    info.append(int(input('idade:')))
    galera.append(info[:])
    print(f"{galera[0]} tem {galera[1]} anos de idade")

