import sys, math

for lin in sys.stdin:
    num = int(lin)
    if(num==0):
        break
    aux = int(math.sqrt(num))
    if (aux*aux==num):
        print('yes')
    else:
        print('no')
