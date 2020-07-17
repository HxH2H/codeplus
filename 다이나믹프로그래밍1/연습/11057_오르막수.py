# 점화식을 잘 기억하자
# 오르막수는 앞에수가 현재 수보다 같거나 작다
import sys
n = int(sys.stdin.readline())
result = [[0]*10 for _ in range(1001)]
for i in range(10):
    result[1][i] = 1
for i in range(2, 1001):
    for j in range(10):
        for k in range(j+1):
            result[i][j] += result[i-1][k]
            result[i][j] %= 10007
print(sum(result[n])%10007)
