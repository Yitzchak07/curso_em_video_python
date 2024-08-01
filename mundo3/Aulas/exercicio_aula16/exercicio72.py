numero = ('zero','Um','dois','tres','quatro','cinco',
'seis','sete','oito','nove','dez','onze','doze','treze',
'cartoze','quinze','dezeseis','dezesete','dezoito','dezenove',
'vinte')
while True:
    n1 = int(input('digite um numero de 0 a 20:'))
    n1 == " "
    if 0 <= n1 <= 20:
        break
   
    print(f"voce digitou o numero {numero[n1]}")

    print("voce quer continuar![S/N]")
    sair = str(input("continuar!:")).strip().upper()

    if sair == "N":
        break
    else:
        n1 = int(input('digite um numero de 0 a 20:'))
        break
print(f"voce digitou o numero {numero[n1]}")

    
