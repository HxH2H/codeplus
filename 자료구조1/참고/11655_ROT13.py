import sys
lo = 'abcdefghijklmnopqrstuvwxyz'
up = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
line = list(sys.stdin.readline().rstrip('\n'))
for i in range(len(line)):
    if line[i].islower():
        idx = lo.index(line[i])
        idx = idx + 13
        if idx > 25:
            idx = idx - 26
        line[i] = lo[idx]
    if line[i].isupper():
        idx = up.index(line[i])
        idx = idx + 13
        if idx > 25:
            idx = idx - 26
        line[i] = up[idx]
for j in line:
    print(j, end='')