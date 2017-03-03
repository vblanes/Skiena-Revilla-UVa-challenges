import sys
from math import ceil
from math import sqrt

ncasos = int(sys.stdin.readline())
for c in range(ncasos):
    aux = sys.stdin.readline().split()
    n = max(int(aux[1]), int(aux[0])) - min(int(aux[1]), int(aux[0]))
    if n > 0:
        print(ceil(sqrt(4*n)-1))
    else:
        print(0)    
