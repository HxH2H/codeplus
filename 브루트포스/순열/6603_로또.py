import sys
def permutation(n):
    i = n-1
    while i > 0 and cor[i-1] >= cor[i]:
        i -= 1
    if i<=0:
        return False
    j = n-1
    while cor[i-1] >= cor[j]:
        j -= 1
    cor[i-1],cor[j] = cor[j], cor[i-1]
    j = n-1
    while i<j:
        cor[i],cor[j] = cor[j],cor[i]
        i += 1
        j -= 1
    return True
while True:
    n , *n_arr = list(map(int, sys.stdin.readline().rstrip().split()))
    if n == 0:
        break
    cor = [0]*(n-6) + [1]*6
    ans = []
    while True:
        cur = [n_arr[i] for i in range(n) if cor[i] == 1]
        ans.append(cur)
        if not permutation(n):
            break
    ans.sort()
    for i in ans:
        print(' '.join(map(str, i)))
    print()