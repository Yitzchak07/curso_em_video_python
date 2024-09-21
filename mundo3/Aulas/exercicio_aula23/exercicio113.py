def leiaint(msg):
    ok = False
    valor = 0
    while True:

        try:
            n = int(input(msg))
            valor = int(n)
        except ValueError:
            print("ERRO: por favor, digite apenas numeros inteiros")
        
        except KeyboardInterrupt:
            print("Usuario preferiu nao informar um valor")
            
        else:

            ok = True
        if ok:
            break
    return valor


def leiafloat(msg):
    ok = False
    valor = 0
    while True:
        try:
            n = float(input(msg))
            valor = float(n)
        except ValueError:
            print("ERRO: por favor, digite apenas numeros Reais ")
        except KeyboardInterrupt:
            print("Usuario preferiu nao informar um valor")
            
        else:
            ok = True
        if ok:
            break
    return valor

n = leiaint("Digite um numero:")
n = leiafloat("Digite um numero Real:")
print(f"voce acabou de digitar o numero {n} e o real e {n}")

