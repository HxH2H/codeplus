import sys
def erastos(n):
    num_list = [True] * (n+1)
    for i in range(2, int((n)**0.5)+1):
        if num_list[i]:
            for j in range(2*i, n+1, i):
                num_list[j] = False
    return [i for i in range(2, n+1) if num_list[i]]
M, N = map(int, sys.stdin.readline().rstrip().split())
prime_list = erastos(N)
for i in prime_list:
    if i >= M:
        print(i)