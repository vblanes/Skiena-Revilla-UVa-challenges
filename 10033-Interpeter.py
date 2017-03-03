import sys

def int_to_str(num):
    if num < 10:
        return '00'+str(num)
    elif num < 100:
        return '0'+str(num)
    else:
        return str(num)


ncasos = int(sys.stdin.readline())
sys.stdin.readline()
for c in range(ncasos):
    regs = [0]*10
    RAM = []
    while True:
        aux = sys.stdin.readline().strip()
        if not aux:
            break
        RAM.append(int(aux))
    while(len(RAM)!=1000):
        RAM.append(0)
    i = 0
    contador = 1
    while(RAM[i]!=100):

        contador+=1
        ins = int_to_str(RAM[i])
        codi = ins[0]
        if codi == '2':
            regs[int(ins[1])] = int(ins[2])
        elif codi == '3':
            regs[int(ins[1])] = ((regs[int(ins[1])] + int(ins[2])) % 1000)
        elif codi == '4':
            regs[int(ins[1])] = ((regs[int(ins[1])] * int(ins[2])) % 1000)
        elif codi == '5':
            regs[int(ins[1])] = regs[int(ins[2])]
        elif codi == '6':
            regs[int(ins[1])] = ((regs[int(ins[1])] + regs[int(ins[2])]) % 1000)
        elif codi == '7':
            regs[int(ins[1])] = ((regs[int(ins[1])] * regs[int(ins[2])]) % 1000)
        elif codi == '8':
            regs[int(ins[1])] = RAM[regs[int(ins[2])]]
        elif codi == '9':
            RAM[regs[int(ins[2])]] = regs[int(ins[1])]
        elif codi=='0':
            if regs[int(ins[2])] != 0:
                i = regs[int(ins[1])]
                continue
        i+=1
    print(contador)
    if c != ncasos-1:
        print('')
