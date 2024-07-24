ano = int(input('informe sua idade para saber qual categoria de natacao voce esta!:'))

idade = 2024 - ano
print(idade)
if idade < 9:
    print("mirim")

elif idade >= 9 and idade <= 14:
    print("infantil")

elif idade >= 15 and idade <= 19:
    print("junior")

elif idade > 19 and idade <= 20:
    print("Senior")

else:
    print("Master")