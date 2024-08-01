frase = ('curso','aprender','programar','python','linguagem','gratis','futuro')


for p in frase:
    print(f"\nNa palavra {p} temos ",end="")
    for letra in p:
        if letra.lower() in "aeiou":
            print(letra ,end="")