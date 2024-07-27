# import math
# print("digite um numero para saber seu fatorial")
# matematica = True

# while matematica == True:
#     n1 = int(input('digite um numero:'))
#     fatotial = math.factorial(n1)
#     print(fatotial)
#     break


n1 = int(input('digite um numero para saber se fatorial:'))
c = n1
f = 1
print("Calculando {}! = ".format(n1),end='')
while c > 0:
    print("{}".format(c),end="")
    print(" x " if c > 1 else " = ",end="")
    f *= c
    c -= 1
print("o Fatorial de {} e {}".format(n1,f))