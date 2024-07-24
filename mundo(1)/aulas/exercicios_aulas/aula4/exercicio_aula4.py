nome = input("digite seu nome: ").lower()

print("bem vindo:",nome)

dia = int(input("digite o dia que voce nasceu: "))
mes = input("digite o dia que voce nasceu: ")
ano = int(input("digite o dia que voce nasceu: "))

idade = ano - 2024

if ano < 2006:
    print("voce e velho")

elif ano >= 2006:
    print("voce e novo")

print(f"esse e o dia do seu nascimento {dia} voce e do mes de {mes} do  ano de {ano}")

nun1 = int(input("digite um numeor"))
nun2 = int(input("digite um numeor"))

result = nun1 + nun2

print(f"esse e o resultado {result}")

print(f"esse e seu nome {nome} essa e sua idade {idade} essa e sua conta de de adicao {result}")
