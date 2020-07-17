# 중복도 없고 오름차순인 수열
import sys
n, m = map(int, sys.stdin.readline().rstrip().split())
check = [False] * (n+1)
ans = [0]*m
def go(index, start, n, m):
    if index == m:
        sys.stdout.write(' '.join(map(str, ans)) + '\n')
        return
    for i in range(start, n+1):
        if check[i]:
            continue
        check[i] = True
        ans[index] = i
        go(index+1, i+1, n, m)
        check[i] = False
go(0,1,n,m)