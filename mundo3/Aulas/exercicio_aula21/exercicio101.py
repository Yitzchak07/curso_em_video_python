import datetime
def votar():

    ano_votacao = int(input("Em que ano voce nasceu?:"))

    ano_nascimento = datetime.datetime.today().year - ano_votacao
    if ano_nascimento > 16 and ano_nascimento < 100:
        return print(f"com {ano_nascimento} Anos e OBRIGATORIO VOTAR!")
    elif ano_nascimento == 16 or ano_nascimento >= 100:
        return print(f"Com {ano_nascimento} Anos e OPCIONAL VOTAR!")
    else:
        return print(f"com {ano_nascimento} Anos Voce nao pode votar!")
votar()