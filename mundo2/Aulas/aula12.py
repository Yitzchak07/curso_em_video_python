nome = str(input('qual e seu nome?:')).strip().capitalize()

# if sozinho e condicional simples!
# if e else e uma estrutura condicional composta!
# if elif e else e uma estrutura condicional aninhada!

if nome == "Isac":
    print("ola {} tudo bem contigo lembre-se nao desista dos seus sonhos!".format(nome))
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Joao':
    print("seu nome em bem popular no Brasil! {}".format(nome))
elif nome in 'Ana Beatriz Isa ':
    print("belo nome feminino! {}".format(nome))
elif nome == 'Isac emanuel':
    print("belo nome e sobrenome")
else:
    print('seu nome e bem normal!')
print('tenha um bom dia, {}!'.format(nome))