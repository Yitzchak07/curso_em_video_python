from datetime import date
totalmaior = 0
totalmenor = 0

atual = date.today().year
for i in range(1,8):
    ano = int(input("em que ano a {}a pessoa nasceu?:".format(i)))
    idade = atual - ano
    if idade >=21:
        totalmaior += 1

    else:
        totalmenor += 1
print("o total de pessoas maior de idade {} ".format(totalmaior), end="")
print(" o total de pessoas menor de idade {}".format(totalmenor))
