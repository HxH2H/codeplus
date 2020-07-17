import sys
n, k = map(int, sys.stdin.readline().rstrip().split())
result = [[0] * (n + 1) for _ in range(k + 1)]
result[0][0] = 1
for i in range(1, k+1):
    for j in range(n + 1):
        result[i][j] = result[i-1][j]
        if j-1 >= 0:
            result[i][j] += result[i][j-1]
        result[i][j] %= 1000000000
print(result[k][n])