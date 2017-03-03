import sys


def to_dicc(cripts, original):
    dicc = {' ':' '}
    for i in range(len(cripts)):
        for j in range(len(cripts[i])):
            cc = cripts[i][j]
            co = original[i][j]
            if cc in dicc and dicc[cc] != co:
                return None
            else:
                dicc[cc] = co
    return dicc

ncasos = int(sys.stdin.readline())
sys.stdin.readline()
clave = 'the quick brown fox jumps over the lazy dog'.split()
for c in range(ncasos):
    criptogramas = []
    posibles_frases = []
    while True:
        aux = sys.stdin.readline().strip()
        if not aux:
            break
        aux = aux.split()
        criptogramas.append(aux)
        #si puede ser la frase de siempre
        if len(aux) == 9:
            bandera = True
            for i in range(9):
                if len(aux[i]) != len(clave[i]):
                    bandera = False
                    break
            if bandera:
                posibles_frases.append(len(criptogramas)-1)
    # comprobar los posibles
    dicc = None
    for opt in posibles_frases:
        dicc = to_dicc(criptogramas[opt], clave)
        if dicc != None:
            break
    # ya tenemos el diccionario correcto
    if dicc is None:
        print('No solution.')
    else:
        for i in range(len(criptogramas)):
            aux = ' '.join(criptogramas[i])
            for char in aux:
                print(dicc[char], end='', flush=True)
            print('')
    if c != ncasos-1:
        print('')
