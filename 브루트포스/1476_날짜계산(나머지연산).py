import sys
E, S, M = map(int, sys.stdin.readline().rstrip().split())
E -= 1
S -= 1
M -= 1
i = 0
while True:
    if i%15 == E and i%28 == S and i%19 == M:
        print(i+1)
        break
    i += 1