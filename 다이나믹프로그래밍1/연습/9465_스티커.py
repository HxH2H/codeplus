import sys
t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    t1 = [0] + list(map(int, sys.stdin.readline().rstrip().split()))
    t2 = [0] + list(map(int, sys.stdin.readline().rstrip().split()))
    sticker = list(zip(t1,t2))
    result = [[0]*3 for _ in range(n+1)]
    for i in range(1, n+1):
        result[i][0] = max(result[i-1])
        result[i][1] = max(result[i-1][0], result[i-1][2]) + sticker[i][0]
        result[i][2] = max(result[i-1][0], result[i-1][1]) + sticker[i][1]
    print(max(result[n]))