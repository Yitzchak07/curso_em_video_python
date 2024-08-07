times = list()
jogador = {}
partidas = []
while True:
    jogador['nome'] = str(input("Digite o nome do jogador!:")).strip()
    total = int(input(f"quantas partidas o {jogador['nome']} jogou:"))
    partidas.clear()

    for p in range(0,total):
        partidas.append(int(input(f"quantos gols o {jogador['nome']} fez na {p} Partida")))
        jogador['gols'] = partidas[:]
        jogador['total'] = sum(partidas)
        times.append(jogador.copy())
    while True:
        resp = str(input("quer continuar[S/N]:")).strip().upper()
        if resp in "SN":
            break
        print("erro")
    if resp == "N":
        break

print("cod",end="")
for i in jogador.keys():
    print(f"{i:<15}",end="")
for k, v in enumerate(times):
    print(f"{k:>4}", end="")
    for d in v.values():
        print(f"{str(d):<15}", end="")
    print()

