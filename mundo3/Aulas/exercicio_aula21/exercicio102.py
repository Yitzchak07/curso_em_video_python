from math import factorial
def fatorial(n,show=False):
    f = 1
    for c in range(n, 0, -1):
        if show:
            print(f"{c}",end="")
            if c>1:
                print(f'x',end="")
            else:
                print(' = ',end="")
        f *= c
        return factorial(n)
print(fatorial(10,show=True))
