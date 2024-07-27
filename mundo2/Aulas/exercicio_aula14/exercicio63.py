n1 = int(input('digite um numero :'))

t1 = 0 
t2 = 1
cont = 3 
while cont <= n1:
    t3 = t1 + t2 
    print(" -> {}".format(t3),end="")
    t1 = t2
    t2 = t3 
    cont += 1
print(" Fim")