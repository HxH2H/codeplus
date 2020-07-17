import sys
n, k = map(int, sys.stdin.readline().rstrip().split())
result = [0]*(n+1)
result[0] = 1
for _ in range(1, k+1):
    for i in range(1, n+1):
        result[i] += result[i-1]
        result[i] %= 1000000000
print(result[n])