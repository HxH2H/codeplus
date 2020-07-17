import sys
n = int(sys.stdin.readline())
result =  [0, 1, 3]
for i in range(3, n + 1):
    result.append((2*result[i-2]) + result[i-1])
print(result[n] % 10007)