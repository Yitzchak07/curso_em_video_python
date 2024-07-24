#crie um programa que leia o nome de um cidade e diga se ela comeca ou nao com o nome "SANTO"

cidade = str(input("digite o nome da sua cidade:").strip())


print(cidade[:5].upper() == "SANTO")