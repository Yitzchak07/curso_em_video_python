# Listas parte 1
# Tuplas = ()
# Listas = []
lanche = ['hamburguer','suco','pizza','pudim']
print(lanche)
lanche[3] = 'picole'
print(lanche)
lanche.append('coockie')# adicionar mais elementos na lista
print(lanche)
lanche.insert(0,'cachorro quente')# adicionar elementos em qualquer posicao 
print(lanche)
#del lanche[3]
#lanche.pop(3)# remove o ultimo elemento da lista
lanche.remove('pizza')
lanche.insert(4,'pizza')
print(lanche)
if 'pizza' in lanche:
    lanche.remove('pizza')
    print(lanche)
#valores = list(range(4,11))
valores = [4,6,1,8,19,7]
valores.sort()# arrumar o valores de formas alinhadas
valores.sort(reverse=True)# corrige os valores de forma reversa
print(len(valores))
print(valores)
print(max(valores))# maior valor
print(min(valores))# menor valor

# n1 = [1,2,7,9,1,2]
# print(n1)
# for cont in range(0,5):
#     n1.append(int(input('digite um numero')))
# if 4 in n1:
#     n1.remove(4)
# else:
#     print("valor 4 nao encontado na lista")
# print(n1)
# for c, v in enumerate(n1):
#     print(f"na posicao {c} valor {v}")

a = [1,3,4,5]
b = a[:]# copia do a
# b = a lincando a mais b   
b[2] = 8
print(a)
print(b)