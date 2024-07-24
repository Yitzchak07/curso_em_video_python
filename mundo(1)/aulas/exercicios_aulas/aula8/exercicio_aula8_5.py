from random import shuffle
aluno1 = input('digite o nome do aluno:')
aluno2 = input('digite o nome de outr aluno:')
aluno3 = input('digite o nome de mais um aluno:')
aluno4 = input('digite outro aluno por favor:')

lista = [aluno1,aluno2,aluno3,aluno4]
shuffle(lista)
print('a lista de apresentacao e ')
print(lista)