# 중복이 없는 수열
import sys
n, m = map(int, sys.stdin.readline().rstrip().split())
check = [False] * (n+1)
ans = [0]*m
def go(index,n,m):
    if index == m:
        sys.stdout.write(' '.join(map(str, ans)) + '\n')
        return
    for i in range(1, n+1):
        if check[i]:
            continue
        check[i] = True
        ans[index] = i
        go(index+1, n, m)
        check[i] = False

go(0, n, m)