def jogador():
    nome_joga = str(input("digite o nome do jogador:")).strip().capitalize()
    gols = str(input("quantidade de gols:")).strip()

    if nome_joga == "" and gols == "":
        nome_joga = "DEsconhecido"
        gols = "0"
    
    print(f"O jogador {nome_joga} Fez {gols} Gol(s) no campeonato.")
    
jogador()