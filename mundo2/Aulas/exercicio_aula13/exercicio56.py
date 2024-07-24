somaidade = 0
mediaidade = 0
maioridadehome = 0
nomemaisvelho = ''
totalmulher20 = 0
for pessoa in range(1,5):
    print("{} PESSOA".format(pessoa))
    nome = str(input('nome da {} pessoa:'.format(pessoa)))
    idade = int(input('idade da {} pessoa:'.format(pessoa)))
    sexo = str(input('[M/F]:'))
    somaidade += idade
    if  pessoa == 1 and sexo in "mM":
        maioridadehome = idade
        nomemaisvelho = nome
    if sexo in "Mm" and idade > maioridadehome:
        maioridadehome = idade
        nomemaisvelho = nome
    if sexo in "fF" and idade < 20:
        totalmulher20 += 1
mediaidade = somaidade / 4
print("a media de idade do grupo e de {:.0f} anos".format(mediaidade))
print("o Homem mais velho tem {} anos e se chama {}".format(maioridadehome,nomemaisvelho))
print("Ao total sao {} mulheres com menos de 20 anos".format(totalmulher20))
