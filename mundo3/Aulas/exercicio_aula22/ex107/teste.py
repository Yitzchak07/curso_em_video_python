from moeda import metade,diminuir,dobro,aumentar

p = float(input("Digite o preco: R$"))
print(f"A metade de R${p} e {metade(p)}")
print(f"O dobro de R${p} e {dobro(p)}")
print(f"O aumento de 10% de R$ {p} e {aumentar(p,10)}")
print(f"o diminuido 13% de {p} e {diminuir(p,13)}")