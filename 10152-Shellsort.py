import sys

ncasos = int(sys.stdin.readline())
for cas in range(ncasos):
    nturtles = int(sys.stdin.readline())
    tortugas = []
    tortugasord = []
    for turt in range(nturtles):
        tortugas.append(sys.stdin.readline())
    for turt in range(nturtles):
        tortugasord.append(sys.stdin.readline())
    ordenacion = []
    for ind in range(nturtles):
        ordenacion.append(tortugasord.index(tortugas[ind]))
    # marca los elementos a mover
    desp = []
    maximo = -1
    for ind in range(nturtles):
        if ordenacion[ind] > maximo:
            maximo = ordenacion[ind]
        else:
            desp.append(tuple((ind, ordenacion[ind])))
    # ordena los cambios
    if len(desp) == 0:
        # print('')
        pass
    else:
        desp.sort(key=lambda tup: tup[1], reverse=True)
        cont = 0
        marcats = []
        for tup in desp:
            marcats.append(tup[0])
        maxim = desp[0][1]

        '''
        for i in range(nturtles-1, -1, -1):
            if i in [x for x,y in enumerate(desp)] or i+cont != ordenacion[i]:
                print(tortugas[i])
                cont+=1
        '''
        cont = 0
        #print(desp)
        #print(marcats)
        for val in range(maxim, -1, -1):
            ind = ordenacion.index(val)
            #print(ind)
            if ind in marcats or tortugas[ind+cont] != tortugasord[ordenacion[ind]]:
                print(tortugas[ind].strip())
                cont+=1

    print('')
