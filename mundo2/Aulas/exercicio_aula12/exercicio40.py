nota1 = float(input('digite a sua nota:'))
nota2 = float(input('digite sua outra nota:'))

media = (nota1 + nota2) / 2
print(media)
if media < 5.0:
    print("voce foi reprovado sua media e {}".format(media))

elif media == 5.0 or media <= 6.9:
    print("voce esta de recuperacao mas nao fique preocupado sua media foi {:.1f}".format(media))
    
elif media >= 7.0:
    print("'PARABENS' Voce passou direto sua media foi {}".format(media))