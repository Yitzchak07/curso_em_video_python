frase = str(input("escreva uma frase:"))
palavras = frase.split()
junto = ''.join(palavras)
iverso = ''
for letra in range(len(junto)-1,-1,-1):
    iverso += junto[letra]
if iverso == junto:
    print("A sua frase e uma palindomo {} e {}".format(junto,iverso))
else:
    print("sua frase nao e um palindromo")