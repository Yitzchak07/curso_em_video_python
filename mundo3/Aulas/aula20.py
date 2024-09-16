# funcoes python

def mostralinha():
    print('-' * 30)
mostralinha()
# def mensagem(msg):
#     print('='*30)
#     print(msg)
#     print('='*30)
# mensagem(str(input('digite sua mensagem:').strip().upper()))
def soma(a, b):
    print(f'A = {a} e B = {b}')
    s = a + b
    print(f'a soma A + B e {s}')

soma(a=5,b=9)
# desempacotar 
def contador(*nun):
    print((type(nun)))
    for valor in nun:
        print(valor, end='-')
    print('fim',end='')

contador(1,4,5,7,4)