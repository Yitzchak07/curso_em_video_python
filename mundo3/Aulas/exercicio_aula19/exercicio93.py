jogador = {}
partidas = []
jogador['nome'] = str(input("Digite o nome do jogador!:")).strip()
total = int(input(f"quantas partidas o {jogador['nome']} jogou:"))

for p in range(0,total):
    partidas.append(int(input(f"quantos gols o {jogador['nome']} fez na {p} Partida")))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)

print(jogador)
print("=" * 30)
for k,v in jogador.items():
    print(f"o campo {k} tem o valor {v}")
    
