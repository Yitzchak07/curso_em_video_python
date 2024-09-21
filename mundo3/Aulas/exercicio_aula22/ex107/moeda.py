def metade(preco):

    resut = preco / 2
    return resut


def dobro(preco):
    resut = preco * 2
    return resut

def aumentar(preco,taxa):

    resut = preco + (preco * taxa/100)
    return resut


def diminuir(preco,taxa):

    resut = preco - (preco * taxa/100)
    return resut