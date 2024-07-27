sexo = str(input('digite seu sexo [M/F]')).strip().upper()[0]

while sexo not in  "MF":
    sexo = str(input('digite novamente:')).strip().upper()[0]
print("sexo {} registrado com sucesso!".format(sexo))
