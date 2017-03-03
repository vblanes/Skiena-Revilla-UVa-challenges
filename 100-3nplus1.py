import sys
cache = [None]*10000000

def ejercicio(i, j):
    # clausura
    def tnp1(num):
        if num == 1:
            return 1
        elif num<len(cache) and cache[num]:
            return cache[num]
        elif num % 2 == 0:
            return tnp1(int(num/2))+1
        else:
            return tnp1(num*3+1)+1
    # prepara los indices
    n1 = min(i, j)
    n2 = max(i, j)
    results = set()
    for k in range(n1, n2+1):
        res = tnp1(k)
        if k < len(cache):
            cache[k] = res
        results.add(res)
    return max(results)

if __name__ == '__main__':
    for lin in sys.stdin:
        try:
            i = int(lin.strip().split(' ')[0])
            j = int(lin.strip().split(' ')[-1])
            print(i, j, ejercicio(i, j))
        except:
            continue
