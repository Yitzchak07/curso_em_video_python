pessoa = 1

while pessoa == 1:
    sexo = 'M' or 'F'
    sexo = str(input('digite uma das opcoes[M/F]:')).upper()
    
    if sexo != 'M' and sexo != 'F':
        print("escolha uma das opcoes")

    elif sexo == 'M' and sexo == 'F':
        break