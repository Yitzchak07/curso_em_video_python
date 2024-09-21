def metade(preco = 0):

    resut = preco / 2
    return print(f"R${preco} R${resut}")


def dobro(preco = 0):
    resut = preco * 2
    return resut

def aumentar(preco = 0,taxa = 0):

    resut = preco + (preco * taxa/100)
    return resut


def diminuir(preco = 0,taxa = 0):

    resut = preco - (preco * taxa/100)
    return resut

def moeda(preco = 0,moeda = 'R$'):
    return f"{moeda} {preco}".replace("," , ",")