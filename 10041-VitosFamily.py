import sys

ncasos = int(sys.stdin.readline())
for cas in range(ncasos):
    # numero de las casas
    vec = [int(x) for x in sys.stdin.readline().split()[1:]]
    # calculo de la mediana
    mediana = sorted(vec)[int(len(vec)/2)]
    cont = 0
    for elem in vec:
        cont+=abs(elem-mediana)
    print(cont)
