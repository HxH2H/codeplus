import sys
def erastos(n):
    num_list = [True] * (n+1)
    for i in range(2, int(n**0.5)+1):
        if num_list[i]:
            for j in range(i*2, n+1, i):
                num_list[j] = False
    return num_list
prime_list = erastos(1000000)
tc = int(sys.stdin.readline())
for _ in range(tc):
    count = 0
    N = int(sys.stdin.readline())
    for i in range(2, N//2 + 1):
        if prime_list[i] and prime_list[N-i]:
            count += 1
    print(count)