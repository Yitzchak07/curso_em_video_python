# Manipulando strings = Texto!

frase = 'Curso em video Python'
#fatiamento
print('_'*20)
print("Fatiamento de String = Str")
# no fatiamento o ultimo numero sempre e ignorado!
print(frase)
print(frase[9])
print(frase[9:13])
print(frase[9:21])
print(frase[9:21:2])
print(frase[:5])
print(frase[15:])
print(frase[9::3])

print("_"*20)
print("Analise de string")

print(len(frase))
print(frase.count('o'))
print(frase.count('r'))
print(frase.count('o',0,13))# vai contar do 0 ate o 13 quantos 'o' existem, semore vai ignora o ultimo numero
print(frase.find('deo'))#procure 'deo' na variavel frase 
print(frase.find("android"))# quando nao existe nada ele exibe -1
print('Curso'in frase)# para receber tudo correto escreva como se fosse uma variavel para nao aver erro!

print("_"*20)
print("transformaçao")

print(frase.replace('Python','android'))# subistituir a palavra Python por android function replace
print(frase.upper())#Faz que Letras Minusculas Fiquem Maiusculas
print(frase.lower())#Faz que Letras Maiusculas Fiquem Minusculas
print(frase.capitalize())# faz que todas as letras fiquem minusculas menos a primeira que for Maiuscula!
print(frase.title())# Faz a leitura das palvras mais aprimorado colocando letras maiusculas em cada quebra de espaço
print(frase.strip)# se tiver espaço antes da palavra ele remove exemplo   oi ele remove e fica oi
print(frase.rstrip())# remove os espaços da direita se ouver algum!
print(frase.lstrip())# remove os espacos da esquerda se ouver algum 
print("_"*20)
print("divisao")

print(frase.split())# vai dividir a palavras exemplos (Curso) (em) (video) (Python)
dividido = frase.split()
print(dividido[0][::])

print("_"*20)
print("jucao")
print("-".join(frase))# Faz a juncao das palavras substituindo os espaços pelo oque voce colocou entre as apas"-"


print("""oi joao robertoo da silva destruidor de mundos ribeiro meteoro da paixao gustavo de lima de sorocaba paulaco de xagas de pabro bruno da silva pinto junior""")