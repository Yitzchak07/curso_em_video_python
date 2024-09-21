
""""
Modularizacao

surgiu no inicio da decada de 60


sistemas ficando 
cada vez maior

foco: dividr um programa grande

foco: aumentar a legibilidade

foco: facilitar a manutencao
"""

def fatorial(n):
    f = 1
    for c in range(1,n+1):
        f*= c
    return f
nun = int(input("digite um numero:"))
fat = fatorial(nun)
print(f"fatorial de {nun} e {fat}")