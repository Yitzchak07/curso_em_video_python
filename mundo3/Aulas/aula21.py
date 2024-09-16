# topicos 
# interatividade help
# docsstrings
# argumentos opcionais 
# escopos de variaveis 
# retorno de resultados

# ajuda interativa interactive help

#help()

#print(input.__doc__)

def contador(i,f,p):
    """
    contador(Inicio,FIM,PASSO)
    inicio comece em tal numero
    fim termine em tal numero
    passo pule de 2 em 2 ou 3 em 3 voce escolhe
    """
    c = i
    while c <= f:
        print(f"{c}",end="")
        c += p
    print("fim")
contador(1,10,2)

help(contador)
def somar(a,b,c=0):
    """
    faz a soma de 3 numero
    param a = primeiro numero
    param b = segundo numero
    param c = terceiro numero caso nao tenha um 3 numero c recebe 0



    """
    s = a + b + c
    print(f"a soma vale {s}")
somar(1,0,5)
help(somar)

