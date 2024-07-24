medida = float(input("uma distancia em metros:"))

cm = medida * 100
mm = medida * 1000
km = medida / 1000
dm = medida *10
dam = medida /10
hm = medida /100
print("{}KM".format(km))
print("{}hm".format(hm))
print("{}dam".format(dam))
print("{:.00f}dm".format(dm))
print("{:.00f}cm".format(cm))
print("{:.00f}mm".format(mm))
print("acabou hihih exercicio feito!")