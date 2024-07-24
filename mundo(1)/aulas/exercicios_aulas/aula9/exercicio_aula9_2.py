#faca um programa que leia um numero de 1 a 9999 e mostre na tela cada um dos digitos separados

#ex (digite um numeor 1834)

#unidade:4
#dezena:3
#centena:8
#milhar:1


#Fiz em str
nun1 = int(input('digite um numeor:'))

u = nun1 // 1 % 10
d = nun1 // 10 %10
c = nun1 // 100 % 10
m = nun1 // 1000 % 10
print("unidade",u)
print("dezena",d)
print("centena",c)
print("milhar",m)

