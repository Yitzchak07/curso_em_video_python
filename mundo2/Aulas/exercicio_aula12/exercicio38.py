n1 = int(input('digite um numero:'))
n2 = int(input('digite outro numero:'))

maior = n1
if n2 > n1:
    menor = n2
    print('o segundo numero que e {} e maior que o primeiro {}'.format(n2,n1))

elif n1 > n2:
    print('o primeiro numero que e {} acaba sendo maior que o segundo que e {}'.format(n1,n2))
elif n1 == n2:
    print('o primeiro numero que e {} tem o mesmo valor que o segundo {} um nao e maior que o outro'.format(n1,n2))

