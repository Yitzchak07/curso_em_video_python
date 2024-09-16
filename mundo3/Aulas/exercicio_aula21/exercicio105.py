def notas(*n, sit=True):
    r = dict()
    r["total"] = len(n)
    r["maior"] = max(n)
    r["menor"] = min(n)
    r["media"] = sum(n)/len(n)
    if sit:
        if r["media"] >= 7:
            r["situacao"] = 'boa'
        elif r["media"] >= 5:
            r["situacao"] = 'rasoavel'
        else:
            r["situacao"] = 'Ruim'
    return r





resp = notas(5.5,2.5,9,8.5)
print(resp)