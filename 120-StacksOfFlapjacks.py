import sys

for lin in sys.stdin:
    # array de diametres
    arr = [int(x) for x in lin.split()]
    # copia el original
    org = arr[:]
    # per comoditat li pegue la volta
    # arr.reverse()
    moviments = []
    colocats = 0
    while(arr!=sorted(arr)):
        maxpos = arr.index(max(arr[:len(arr)-colocats]))
        if maxpos == 0:
            moviments.append(1+colocats)
            aux = arr[:len(arr)-colocats]
            aux.reverse()
            arr = aux+arr[len(arr)-colocats:]
            colocats+=1
        else:
            aux = arr[:maxpos+1]
            aux.reverse()
            arr = aux+arr[maxpos+1:]
            moviments.append(len(arr)-maxpos)
    #moviments.reverse()
    moviments.append(0)
    print(" ".join([str(x) for x in org]))
    print(" ".join([str(x) for x in moviments]))
