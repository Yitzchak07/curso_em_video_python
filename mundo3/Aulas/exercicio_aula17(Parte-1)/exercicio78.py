nun = [int(input('digite um valor:')),int(input('digite outro valor:')),int(input('digite outro valor:')),int(input('digite mais outro valor:')),int(input('mais um valor:'))]

print("=-"*30)
print(f"O maior valor digitado foi {max(nun)} na posicao {nun.index(max(nun))}")
print(f"o menor valor digitado foi {min(nun)} na posicao {nun.index(min(nun))}")
