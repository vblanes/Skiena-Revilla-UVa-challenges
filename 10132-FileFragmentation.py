import sys

ncasos = int(sys.stdin.readline())
sys.stdin.readline()
for cas in range(ncasos):
    #diccionario longuitud : fragmentos
    files = dict()
    while True:
        aux = sys.stdin.readline().strip()
        # si es linea vacia hasta luego lucas
        if not aux:
            break
        if len(aux) in files:
            files[len(aux)].append(aux)
        else:
            files[len(aux)] = [aux]
    #ya tengo los fragmentos agrupados por tamanyo
    indices = sorted(files.keys())
    combinaciones = []
    i = 0
    j = len(indices)-1
    while i<=j:
        conjunto = set()
        aux1 = files[indices[i]]
        aux2 = files[indices[j]]
        for me in aux1:
            for gr in aux2:
                conjunto.add(me+gr)
                conjunto.add(gr+me)
        combinaciones.append(conjunto)
        i+=1
        j-=1
    #hago and para todos los sets
    discrim = combinaciones[0]
    for i in range(len(combinaciones)-1):
        discrim = discrim.intersection(combinaciones[i+1])
    print(list(discrim)[0])
    if cas < ncasos-1:
        print('')
