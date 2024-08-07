galera = list()
pessoa = dict()
soma = media = 0
while True:
    pessoa.clear()
    pessoa['nome'] = str(input("Digite seu nome:")).strip()
    while True:
        pessoa['sexo'] = str(input("[M/F]:")).strip().upper()
        if pessoa['sexo'] in 'MF':
            break
    pessoa['idade'] = int(input("digite sua idade:"))
    galera.append(pessoa.copy())
    soma += pessoa["idade"]
    
    while True:
        resp = str(input("deseja sair [S/N]:")).upper().strip()
        if resp in "SN":
            print("digite apenas [M/F]")
            break
    if resp == "S":
        break

print(f"ao todo temos {len(galera)} pessoas cadastradas")
media = soma / len(galera)
print(f"a media de idade e {media:.2f} anos.")
print(f" as mulheres cadastradas foram ",end="")
for p in galera:
    if p['sexo'] in 'fF':
        print(f"{p['nome']} ",end="")
print()
print(f" lista das pessoa que estao acima da media. ")
for p in galera:
    if p['idade'] >= media:
        print("    ")
        for k,v in p.items():
            print(f'{k} = {v};',end="")
        print()
print("encerrado!")
