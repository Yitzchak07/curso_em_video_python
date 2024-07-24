dias = int(input("quantos dias alugados?:"))
km = float(input("quantos kms rodados?:"))

pagos = (dias * 60) + (km * 0.15)

print(f"valor final e R${pagos:.02f}")