def notas(*n, siyt=False):
    r = dict()
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['média'] = sum(n)/len(n)

    return r

# Programa Principal
resp = notas(5.5, 2.5, 9, 8.5)
print(resp)
