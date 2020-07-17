import sys
n, m = map(int, sys.stdin.readline().rstrip().split())
ans = [0]*m
def go(index, selected, n, m):
    if selected == m:
        sys.stdout.write(' '.join(map(str, ans)) + '\n')
        return
    if index > n:
        return
    ans[selected] = index
    go(index+1, selected+1, n, m)
    ans[selected] = 0
    go(index+1, selected, n, m)
go(1, 0, n, m)