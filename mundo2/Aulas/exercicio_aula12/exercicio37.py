numero = int(input('digite um numero inteiro:'))
print(""" Escolha um das bases de Conversao:
[1] converter para Binario
[2] converter Para octal
[3] converter para hexadecimal""")

opcao = int(input('Escolha uma opcao!:'))
if opcao == 1:
    print("{} convertido para Binario e {}".format(numero,bin(numero)[2:]))
elif opcao == 2:
    print("{} convertido para octal e {}".format(numero,oct(numero)[2:]))

elif opcao == 3:
    print("{} convertido para hexadecimal e {}".format(numero,hex(numero)[2:]))
else:
    print("escolha uma opcao Valida!")