preco = float(input("qual o preço do produto?:"))

desc = preco - (preco * 5/100)

print(f"o produto que custava R${preco}, agora com o cupom de desconto de 5% vai ficar por R${desc:.01f} ")
print("_"*8)
valor = float(input("digite o valor do produto R$:"))

valor_final = valor - (valor * 10/100)
avista = valor - (valor * 10/100)
parcelado = valor + (valor * 8/100)

print(f"o valor original do produto e R${valor:.02f} comprando avista voce ganha 10% de desconto R${avista:.02f} agora parcelado com juros tem 8% de aumento que fica {parcelado} ")

