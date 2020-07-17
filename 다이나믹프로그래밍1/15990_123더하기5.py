import sys
tc = int(sys.stdin.readline())
result = [[0]*4 for _ in range(100001)]
for i in range(1, 100001):
    if i-1>=0:
        result[i][1] = result[i-1][2] + result[i-1][3]
        if i == 1:
            result[i][1] = 1
    if i-2>=0:
        result[i][2] = result[i-2][1] + result[i-2][3]
        if i== 2:
            result[i][2] = 1
    if i-3>=0:
        result[i][3] = result[i-3][1] + result[i-3][2]
        if i==3:
            result[i][3] = 1
    result[i][1] %= 1000000009
    result[i][2] %= 1000000009
    result[i][3] %= 1000000009
for _ in range(tc):
    n = int(sys.stdin.readline())
    print(sum(result[n])%1000000009)