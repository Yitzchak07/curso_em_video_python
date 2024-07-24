# faca um programa que leia o nome completo de uma pessoa e mostre

#(1) nome com todas as letras em maiusculo!
nome = str(input('digite seu nome:')).strip()
print("seu nome em maiusculas{}".format(nome.upper()))
#(2)nome todo em minusculo
print("seu nome em minusculas{}".format(nome.lower()))

#(3)quantas letras tem ao todos(sem considera os espaços)
print("seu nome tem {} letras".format(len(nome)-nome.count(" ")))

#(4)quantas letras tem o primeiro nome
print("seu primeiro nome tem {} letras".format(nome.find(" ")))
separa = nome.split()
print(separa)