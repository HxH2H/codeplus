import sys
n = int(sys.stdin.readline())
P = [0]
for x in list(map(int,sys.stdin.readline().rstrip().split())):
    P.append(x)
result = [0] * (n+1)
for i in range(1, n+1):
    for j in range(1, i+1):
        result[i] = max(result[i], result[i-j] + P[j])
print(result[n])