print("formas de pagamento")
print("-"*10)
print("avista em dinheiro ou cheque digite (1)")
print("avista no cartao digite (2)")
print("dividido em 2x no cartao digite (3)")
print("dividido em 3x co cartao digite (4) Lembrando aceitamos o pagamento em apenas 3x", end="")
print(" pq nossos produtos sao baratos")
print("-"*10)



produto = float(input('qual o valor do produto?:'))
pagamento = str(input('qual metodo de pagamento?:')).strip()

print("esse e o valor do Protudo R${}".format(produto))


avista = produto - (produto * 10/100)# pagamento avista ou no pix ou cheque
avista_cartao = produto - (produto* 5/100)# pagamento avista no cartao de
parcelado3x = produto + (produto* 20/100) 

if pagamento == "1":
    print("pagando avista em dinheiro ou em cheque voce tem (10%) de desconto R${}".format(avista))

elif pagamento == "2":
    print("pagando avista no cartao voce recebe (5%) de desconto R${}".format(avista_cartao))

elif pagamento == "3":
    print("pagando em 2x no cartao o preco e R${}".format(produto))
elif pagamento == "4":
    print("pagando em 3x no cartao que tem juros de (20%) fica {}".format(parcelado3x))
else:
    print("sua comprar no valor R${} vai ficar por R${} voce nao escolheu metodo de pagamento".format(produto,produto))

