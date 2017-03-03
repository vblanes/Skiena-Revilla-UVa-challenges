import sys

ncasostest = int(sys.stdin.readline())
for caso in range(ncasostest):
    days = int(sys.stdin.readline())
    nparties = int(sys.stdin.readline())
    #parties = [int(sys.stdin.readline()) for x in range(nparties)]
    parties = []
    for c in range(nparties):
        parties.append(int(sys.stdin.readline()))
    conjunto = set()
    for p in parties:
        cont = 0
        while(cont<=days):
            cont+=p
            if cont <= days and not (cont % 7 == 6 or cont % 7 == 0):
                conjunto.add(cont)

    print(len(conjunto))
