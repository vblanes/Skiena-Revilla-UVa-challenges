import sys

def por_valor(carta):
    if carta[0] == 'T':
        return 10
    elif carta[0] == 'J':
        return 11
    elif carta[0] == 'Q':
        return 12
    elif carta[0] == 'K':
        return 13
    elif carta[0] == 'A':
        return 14
    else:
        return int(carta[0])

def puntua_mano(dicc_palo, dicc_num):
    # condicion escalera de colord
    if any(len(x) == 5 for x in dicc_palo.values()):
        numerets = sorted(dicc_num.keys())
        band = True
        for i in range(len(numerets)-1):
            if numerets[i]+1 != numerets[i+1]:
                band = False
        if band:
            return (9, max(numerets))
    # Poker
    if any(len(x) == 4 for x in dicc_num.values()):
        for k in dicc_num:
            if len(dicc_num[k]) == 4:
                return (8, k)
    # full
    val_nums = dicc_num.values()
    if any(len(x) == 3 for x in val_nums) and any(len(x) == 2 for x in val_nums):
        for k in dicc_num:
            if(len(dicc_num[k])==3):
                return (7, k)
    # colord
    if any(len(x)==5 for x in dicc_palo.values()):
        return (6, sorted(dicc_num.keys(), reverse=True))
    #escalera
    numerets = dicc_num.keys()
    if len(numerets) == 5:
        numerets = sorted(numerets)
        band = True
        for i in range(4):
            if numerets[i]+1 != numerets[i+1]:
                band = False
        if band:
            return (5, max(numerets))
    #trio
    if any(len(x) == 3 for x in dicc_num.values()):
        for k in dicc_num:
            if len(dicc_num[k])==3:
                return (4, k)
    # doble parejas
    cont = 0
    val = []
    for k in dicc_num:
        if len(dicc_num[k]) == 2:
            cont+=1
            val.append(k)
    if cont == 2:
        val = sorted(val, reverse=True)
        for k in dicc_num.keys():
            if k not in val:
                val.append(k)
        return (3, val)
    # pareja
    if any(len(x) == 2 for x in dicc_num.values()):
        res = []
        for k in dicc_num.keys():

            if len(dicc_num[k])==2:

                res.append(k)
            for el in sorted(dicc_num.keys()):
                if el not in res:
                    res.append(el)

        return (2, res)
    #mes alta
    return (1, sorted(dicc_num.keys(), reverse=True))





for mano in sys.stdin:
    cartas = mano.split()
    black = sorted(cartas[:5], key = lambda x: por_valor(x))
    white = sorted(cartas[5:], key = lambda x: por_valor(x))
    # diccionario por palo
    por_palo_w = {'C': [], 'D':[], 'H':[], 'S':[]}
    por_palo_b = {'C': [], 'D':[], 'H':[], 'S':[]}
    # clasifique
    for elem in white:
        por_palo_w[elem[1]].append(elem)
    for elem in black:
        por_palo_b[elem[1]].append(elem)
    # diccionario por numero
    por_numero_w = dict()
    por_numero_b = dict()
    for elem in white:
        aux = por_valor(elem[0])
        if aux in por_numero_w:
            por_numero_w[aux].append(elem)
        else:
            por_numero_w[aux] = [elem]
    # lo mateix per al negre
    for elem in black:
        aux = por_valor(elem[0])
        if aux in por_numero_b:
            por_numero_b[aux].append(elem)
        else:
            por_numero_b[aux] = [elem]
    # puntuasion
    puntw = puntua_mano(por_palo_w, por_numero_w)
    puntb = puntua_mano(por_palo_b, por_numero_b)
    #print(puntw)
    #print(puntb)
    if puntb[0] > puntw[0]:
        print('Black wins.')
    elif puntb[0] < puntw[0]:
         print('White wins.')
    else:
        res = 0
        if puntb[0] == 3 or puntb[0] == 1 or puntb[0]==6 or puntb[0] == 2:
            # tengo que comparar listas
            for i in range(len(puntw[1])):
                if puntb[1][i] > puntw[1][i]:
                    res = 1
                    break
                elif puntb[1][i] < puntw[1][i]:
                    res = -1
                    break
        else:
            res = puntb[1]-puntw[1]
        if res > 0:
            print('Black wins.')
        elif res < 0:
             print('White wins.')
        else:
            print('Tie.')
