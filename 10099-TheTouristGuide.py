import sys

while True:
    lin = sys.stdin.readline().split()
    N = int(lin[0])
    R = int(lin[1])
    if N == 0 and R == 0:
        print('')
        break
