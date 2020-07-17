import sys
n,m = map(int, sys.stdin.readline().rstrip().split())
ans = [0]*m
def go(index, start, n, m):
    if index == m:
        sys.stdout.write(' '.join(map(str, ans))+'\n')
        return
    for i in range(start, n+1):
        ans[index] = i
        go(index+1, i, n, m)
go(0, 1, n, m)