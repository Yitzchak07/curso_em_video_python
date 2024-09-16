def ajuda(com):
    help(com)

comando = ''
while True:
    comando = str(input("funcao ou blibioteca > "))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)