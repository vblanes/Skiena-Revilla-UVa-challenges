import sys


def distance_to(fecha1, fecha2):
    sec1 = fecha1[0]*1440+fecha1[1]*60+fecha1[2]
    sec2 = fecha2[0]*1440+fecha2[1]*60+fecha2[2]
    return abs(sec1-sec2)

def to_mins(fecha):
    aux = [int(x) for x in fecha.split(':')[1:]]
    return aux[0]*1440+aux[1]*60+aux[2]


ncasos = int(sys.stdin.readline())
# blanco
sys.stdin.readline()
for cas in range(ncasos):
    #pillo los precios
    precios = [int(x) for x in sys.stdin.readline().split()]
    lineas = []
    while True:
        lin = sys.stdin.readline().strip()
        # cuando encuentre la linea en blanco me detengo
        if not lin:
            break
        lineas.append(lin.split())
    dicc = dict()
    #ordeno por fecha
    #a = sorted(a, key=lambda x: x.modified, reverse=True)
    lineas = sorted(lineas, key=lambda k: to_mins(k[1]))
    for lin in lineas:
        if lin[0] in dicc:
            hist = dicc[lin[0]]
            if (hist[0] and lin[2] in 'enter') or (not hist[0] and lin[2] in 'exit'):
                hist.append(lin[1:])
                hist[0] = not hist[0]
            elif (not hist[0] and lin[2] in 'enter'):
                hist[-1] = lin[1:]
        else:
            if lin[2] in 'enter':
                # si no estaba en el diccionario lo anyadimos
                dicc[lin[0]] = [False, lin[1:]]
    # aqui ya tengo el diccionario completo
    # preparo la factura
    for matricula in sorted(dicc.keys()):
        #print(matricula ,dicc[matricula])
        contador = 2
        aux = dicc[matricula][1:]
        # si solo hay un registro no ha usado la carretera, es 0
        if len(aux)<=1:
            continue
        for i in range(0, len(aux), 2):
            if i == len(aux)-1:
                continue
            #la hora es siempre la de entrada
            hora = int(aux[i][0].split(':')[2]) #if 'enter' in aux[i][1] else int(aux[i+1][0].split(':')[2])
            contador += ((precios[hora]/100)*abs(int(aux[i][2])-int(aux[i+1][2]))+1)
        print(matricula, '$'+ format(contador, '.2f'))
    if cas != ncasos-1:
        print('')
