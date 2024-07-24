nome = str(input('digite seu nome:')).strip()
n = nome.split()
print('seu primeiro nome e {}'.format(n[0]))
print('seu ultimo nome e {}'.format(n[len(n)-1]))
