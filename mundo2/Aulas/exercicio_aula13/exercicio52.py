nun = int(input('digite um numero:'))
total = 0
for i in range(1,nun + 1):

    if nun % i == 0:
        print("\033[33m",end='')
        total += 1

    else:
        print("\033[31m",end='')
    print('{}'.format(i),end='')
          
print("\n\033[mO numero {} foi divisivel {} vezes".format(nun,total))
if total == 2:
    print("o numero {} e Primo".format(nun))
else:
    print("o numero {} nao e primo".format(nun))
       