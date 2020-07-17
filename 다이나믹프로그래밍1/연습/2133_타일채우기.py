import sys
n = int(sys.stdin.readline())
result = [0] * (n+1)
result[0] = 1
for i in range(2, n+1, 2):
    result[i] = 3 * result[i-2]
    for j in range(i-4, -1, -2):
        result[i] += 2 * result[j]
print(result[n])