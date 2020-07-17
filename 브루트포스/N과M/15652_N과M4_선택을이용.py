# 그닥 좋은 방법은 아님 (중복이 가능하기 때문에)
import sys
n, m =map(int, sys.stdin.readline().rstrip().split())
ans = [0]*(n+1)
def go(index, selected, n, m):
    if selected == m:
        for i in range(1, n+1):
            for j in range(ans[i]):
                print(i, end=' ')
        print()
        return
    if index > n:
        return
    for i in range(m - selected, 0, -1):
        ans[index] = i
        go(index+1, selected+i, n, m)
    ans[index] = 0
    go(index+1, selected, n, m)
go(1,0,n,m)