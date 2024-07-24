salario = float(input("digite o salario de um funcionario R$:"))

reajuste = salario + (salario *15/100)

print(f"o fincionario que ganhava {salario} agora com 15% de aumento vai ganhar {reajuste:.02f}")
print("_"*20)
novo_salario = float(input('digite seu salario R$:'))

salario_novo = novo_salario - (novo_salario * 5/100)
print(f"o funcionario que antes recebia R${novo_salario} agora com a diminuiçao do salario de 5% vai receber R${salario_novo}")
