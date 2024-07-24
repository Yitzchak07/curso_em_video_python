"""
Escreva um programa para aprovar emprestimos bancarios para comprar de uma casa,
o programador vai perguntar o valor da casa, o salario do comprador e em quantos anos ele vai pagar

calcule o valor da prestacao mensal sabendo que ela nao pode exceder 30% do salario ou entao o emprestimo
será negado!
"""

casa = float(input('qual o valor da casa?:R$'))

salario = float(input('qual o valor do seu salario?:R$'))
minimo = salario * 30 /100
anos = int(input('qual tempo do financiamento?:'))
prestacao = casa / (anos * 12)
print("para pagar uma casa de R${:.2f} em {} anos".format(casa,anos), end="")
print(" o valor da prestacao sera de R${:.2f}".format(prestacao))
print('prestacao {:.2f} e minimo {:.2f}'.format(prestacao,minimo))
if prestacao <= minimo:
    print("emprestimo ACEITO")
else:
    print("emprestimo NEGADO")