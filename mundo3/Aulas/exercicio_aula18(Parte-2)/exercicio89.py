ficha = list()
while True:
    nome = str(input("nome:"))
    nota1 = float(input("primeira nota:"))
    nota2 = float(input("segunda nota:"))
    media = nota1 + nota2 / 2
    ficha.append([nome,[nota1,nota2],media])
    resp = str(input('deseja continuar[S/N]:')).upper().strip()
    if resp == "N":
        break
print("=" * 30)

print("=" * 30)
for i, a in enumerate(ficha):
    print(f'{1:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    print("_" * 35)
    opc = int(input("mostrar notas de qual aluno 999 para:"))
    if opc == 999:
        break
    if opc <= len(ficha) - 1:
        print(f"notas de {ficha[opc][0]} sao {ficha[opc][1]}")

print('<<< VOLTE SEMPRE >>>')
