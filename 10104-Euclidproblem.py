import sys


def mcd (a, b, x, y):
    #cas base recursio
    if a == 0:
        return b, 0, 1
    #vas reduint el primer nombre hasta 0
    x1, y1 = None, None
    d, x1, y1 = mcd(b%a, a, x1, y1)
    #divisio entera
    x = y1 - (b//a) * x1
    y = x1
    return d, x, y


for lin in sys.stdin:
    aux = lin.split()
    a = int(aux[0])
    b = int(aux[1])
    d, x, y = mcd(a, b, 0, 0)
    if a == b:
        print('0', '1', str(a))
        continue
    print(x, y, d)
