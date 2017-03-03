import sys

fibs = [1,1,2]
for i in range(3,501):
    fibs.append(fibs[i-1]+fibs[i-2])

text = sys.stdin.read().split('\n')
for i in range(len(text)):
    aux = text[i].split()
    a = int(aux[0])
    b = int(aux[1])
    if a == 0 and b == 0:
        break
    if a == 0 and b == 1:
        print(1)
        continue
    if a == 1 and b == 1:
        print(1)
        continue
    cont = 0
    for i in range(1, len(fibs)):
        if fibs[i] >= a and fibs[i] <=b:
            cont+=1
        elif fibs[i] > b:
            break
    if i != len(text)-1:
        print(cont)
    else:
        print(cont, end='', flush=True)
