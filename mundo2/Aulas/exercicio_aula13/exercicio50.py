for d in range(2,101,2):
    print(d)

soma = 0
for c in range(0,6):
    n1 = int(input("digite pares para fazer a soma:"))
    result = n1 % 2
    
    if result % 2 == 0:
        soma += n1
        print(soma)
    
        
    else:
        print("O numero {} nao e par Entao nao da para fazer a conta!".format(n1))
        
print("a soma de todos os numeros par e {}".format(soma))
    
