import sys
n = int(sys.stdin.readline())
n_list = list(map(int, sys.stdin.readline().rstrip().split()))
result = [1]*n
idx = [-1]*n
for i in range(1, n):
    for j in range(i):
        if n_list[i] > n_list[j] and result[j] + 1 > result[i]:
            result[i] = result[j]+1
            idx[i] = j
ans = max(result)
print(ans)
p = [i for i,x in enumerate(result) if x == ans][0]
def find(a):
    if a == -1:
        return
    find(idx[a])
    print(n_list[a], end=' ')
find(p)
print()