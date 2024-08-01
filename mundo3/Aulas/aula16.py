# variaveis compostas tuplas
# as Tuplas Sao Imutavies
# lanche = 'hamburguer' # variavel simples!
# lanche ()=tuplas[]=lista{}=dicionario

lanche = 'hamburguer','suco','pizza','pudim','batata frita' # estrutura composta tuplas!
print(lanche[1:4])
print(f"voce tem lanche {len(lanche)}")
# lanche[2] = 'refrigerante' tuplas sao imutaveis!
print("-"*10)
# for c in lanche:
#     print(f'eu vou comer {c}',end=": ")
for cont in range(0,len(lanche)):
    print(lanche[cont],cont)
print("="*20)
for pos,comida in enumerate(lanche):
    print(f"Eu vou comer {comida} na posicao {pos}")
print("comi pra caramba!")
print("="*10)
print(sorted(lanche))
print(lanche)

print("="*10)
a = (2,5,4)
b = (5,8,1,2)
c = a + b
print(c)
print(f"a variavel c tem {len(c)} elementos")
print(c.count(5))
print(c.index(8))
pessoa = ("Isac",17,"M",85.89)
# del(pessoa) deletar uma tupla
print(f"nome {pessoa[0]} idade {pessoa[1]} sexo {pessoa[2]} peso {pessoa[3]}kg")