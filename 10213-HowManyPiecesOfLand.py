import sys
from math import pow

ncasos = int(sys.stdin.readline())
for c in range(ncasos):
    n = int(sys.stdin.readline())
    #res =   (n*(n-1)/2) + (n*(n-1)*(n-2)*(n-3)/24) + 1
    # la formula no dona be, ho fem com a gilis
    b = n*(n-1)
    b = b*(n-2)
    b = b*(n-3)
    b = b // 24
    c = n*(n-1)
    c = c // 2
    b = b + c
    res = b+1
    print(int(res))
