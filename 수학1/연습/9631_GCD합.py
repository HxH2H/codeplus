import sys
def GCD(a, b):
    if b == 0:
        return a
    return GCD(b, a%b)
tc = int(sys.stdin.readline())
for _ in range(tc):
    t = list(map(int,sys.stdin.readline().rstrip().split()))
    result = 0
    n = t[0]
    n_list = t[1:]
    for i in range(n-1):
        for j in range(i+1, n):
            result += GCD(n_list[i], n_list[j])
    print(result)