import sys
import re

ndict = int(sys.stdin.readline())
# agrupo las palabras por longuitud
frec = dict()
for i in range(ndict):
    aux = sys.stdin.readline().strip()
    if len(aux) in frec:
        frec[len(aux)].append(aux)
    else:
        frec[len(aux)] = [aux]
criptogramas = []
while True:
    linea = sys.stdin.readline().strip()
    if not linea:
        break
    criptogramas.append(linea)


for cripto in criptogramas:
    criptopals = cripto.split()
    #res = backtracking(criptopals)
    #variables para la clausurita
    sol = []
    d = dict()
    # clausura bt
    def bt(s, d):
        if len(s) == len(criptopals):
            return s
        #elif len(s) < len(criptopals):
        else:
            crip = criptopals[len(s)]
            opts = frec[len(crip)]
            for o in opts:
                sol_ = s[:]
                #test = check_colisions(o, crip, dict(d))
                test = dict(d)
                for i in range(len(crip)):
                    if crip[i] in test and test[crip[i]] != o[i]:
                        test = None
                        break
                    else:
                        test[crip[i]] = o[i]

                if test is not None and len(test.keys()) == len(set(test.values())):
                    sol_.append(o)
                    r = bt(sol_, test)
                    if r:
                        return r
        return None
    res = bt(sol, d)
    if res is None:
        print(re.sub('[a-z]', "*"," ".join(criptopals)))
    else:
        print(" ".join(res))
