try:
    n1 = int(input("digite um numero:"))
    n2 = int(input("outro numero:"))
    r = n1 / n2
except ZeroDivisionError:
    print("Nao e possivel fazer uma divisao com Zero")
except ValueError:
    print("DIgite apenas Numeros")
else:
    print(f"O resultado e {r}")
finally:
    print("volte sempre")