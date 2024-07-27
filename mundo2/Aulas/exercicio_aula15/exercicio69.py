mulhermenosde20 = homens = mais18 = 0
while True:
    idade = int(input('digite sua idade:'))
    sexo = ' ' 
    while sexo not in "FM":
        sexo = str(input('Sexo [M/F]')).upper().strip()[0]
    continuar = ' '
    while continuar not in "SN":
        continuar = str(input("deseja continuar[S/N]?:")).upper().strip()[0]
    
    if idade >= 18:
        mais18 += 1
    
    if sexo == "M":
        homens += 1
    
    if sexo == "F" and idade < 20:
        mulhermenosde20 += 1
    
    if continuar == "N" and continuar != "n":
        break
    print("="*20)
print(f"quantas pessoa tem mais de 18: {mais18} pessoa tem +18")
print(f"total de Homens cadastrados {homens}")
print(f"{mulhermenosde20} mulheres tem menos de 20")