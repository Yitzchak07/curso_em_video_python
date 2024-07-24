# lendo a altura e peso para saber seu imc indice de massa corporal
peso = float(input('qual e seu peso!:'))
altura = float(input('qual e sua altura?:'))

imc = peso / (altura ** 2)# calculo de imc
print("seu imc e {:.1f} ".format(imc))
if imc <= 18.5:
    print("Abaixo do peso")
elif imc >= 18.5 and imc < 24.9:
    print("peso ideal")

elif imc >= 25 and imc < 29.9:
    print("sobrepeso")
elif imc >= 30 and imc < 39.9:
    print("obesidade!")
else:
    print("obesidade morbida")