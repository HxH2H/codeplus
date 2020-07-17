import sys
# 방법 1
n = int(sys.stdin.readline())
P = [0]
for x in list(map(int,sys.stdin.readline().rstrip().split())):
    P.append(x)
result = [10000000] * (n+1)
# result = [-1] * (n+1)
result[0] = 0
for i in range(1, n+1):
    for j in range(1,i+1):
        result[i] = min(result[i], result[i-j]+P[j])
        # if result[i] == -1 or result[i] > result[i-j] + P[j]:
        #     result[i] = result[i-j] + P[j]
print(result[n])

