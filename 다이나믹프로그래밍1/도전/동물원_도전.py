# 1차원 배열로 풀어보기
import sys
n = int(sys.stdin.readline())
cage = [0] * (n+1)
result = [0] * (n+1)
cage[0] = 1
result[0] = 1
cage[1] = 2
result[1] = cage[0] + cage[1]
for i in range(2, n+1):
    cage[i] = cage[i-1] + (2*(result[i-2]))
    result[i] = result[i-1] + cage[i]
    cage[i] %= 9901
    result[i] %= 9901
print(result[n] % 9901)