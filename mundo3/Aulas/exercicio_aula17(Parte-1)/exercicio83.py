expre = str(input('digite sua espresssao:')).strip()
pilha = []
for simb in expre:
    if simb == "(":
        pilha.append('(')
    elif simb == ")":
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print("sua espressao esta correta!")
else:
    print("sua espressao esta errada")