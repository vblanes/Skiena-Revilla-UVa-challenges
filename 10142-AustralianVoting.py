from sys import stdin

if __name__ == '__main__':
    # numero de casos de prueba
    ncasostest = int(stdin.readline().strip())
    # linea en blanco
    stdin.readline()
    for t in range(ncasostest):
        # numero de candidatos
        ncandidatos = int(stdin.readline().strip())
        # recoge el nombre de los candidatos
        candidatos = [None]
        for i in range(ncandidatos):
            candidatos.append(stdin.readline().strip())
        # ahora lee las papeletas
        papeletas = []
        aux = stdin.readline().strip()
        while(aux):
            # guardamos las papeletas como un array de enteros
            papeletas.append([int(x) for x in aux.split(' ')])
            aux = stdin.readline().strip()

        # aqui ya tenemos los datos
        while True:
            # cuenta los votos
            contador = dict()
            for papeleta in papeletas:
                if papeleta[0] in contador:
                    contador[papeleta[0]] += 1
                else:
                    contador[papeleta[0]] = 1
            # DEBUG
            #for k in sorted(contador.keys()):
            #    print(k, '->', contador[k])
            #print('=====')
            # comprobacion del maximo
            maximo = max(contador, key=contador.get)
            if contador[maximo]*2 > len(papeletas):
                print(candidatos[maximo])
                break
            # comprobacion empate
            if len(set(contador.values()))<=1:
                for c in sorted(contador.keys()):
                    print(candidatos[c])
                break
            # si no es uno de los casos de detencion y hay que eliminar os minimos
            # valores minimos
            minimos = []
            for k in contador:
                if contador[k] == min(contador.values()):
                    minimos.append(k)
            minimos = sorted(minimos, reverse=True)
            for m in minimos:
                for papeleta in papeletas:
                    papeleta.remove(m)
        if t != ncasostest-1:
            print('')
