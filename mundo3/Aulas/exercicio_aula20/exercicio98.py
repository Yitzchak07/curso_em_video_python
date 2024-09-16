from time import sleep
def linha():
    print("-="*20)

def contagem(i,f,p):
   
    linha()
    print(f"contagem de {i} ate {f} de {p} em {p}")
    linha()
              
    if p < 0:
        p *= -1 
    if p == 0:
        p = 1


    if i < f:
        cont = i
        while cont <= f:
                print(f"{cont}",end=" ",flush=True)
                sleep(0.5)
                cont += p
        print("fim")
    else:
        cont = i 
        while cont >= f:
              print(f"{cont}",end=" ",flush=True)
              sleep(0.5)
              cont -= p
        print("fim")
contagem(1,10,1)
contagem(10,0,2)
ini = int(input("inicio:"))
fim = int(input("fim:"))
passo = int(input("passo:"))
contagem(ini,fim,passo)