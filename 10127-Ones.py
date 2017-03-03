import sys

for inp in sys.stdin:
    inp = int(inp)
    start = '1'
    while True:
        if int(start) % inp == 0:
            print(len(start))
            break
        start+='1'        
