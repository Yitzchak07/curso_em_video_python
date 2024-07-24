#faca um programa que leia uma frase pelo teclado e mostre
frase = str(input('digite um frase:')).upper().strip()
#quantas vezes aparece a letra a
print("aletra A aparece {} vezes".format(frase.count('A')))
#em qual posicao ela aparece pela primeira vez
print("a primeira letra A apareceu na posicao {}".format(frase.find("A")+1))

#em qual possisao ela aparece pela ultima vez 
print("a ultima posicao da letra A e {}".format(frase.rfind("A")+1))
 