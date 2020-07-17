import sys
def erastos(n):
    num_list = [True] * (n+1)
    for i in range(2, int(n**0.5)+1):
        if num_list:
            for j in range(2*i, n+1, i):
                num_list[j] = False
    return num_list
prime_list = erastos(1000000)
while True:
    N = int(sys.stdin.readline())
    if N == 0:
        break
    for i in range(3, N//2 + 1):
        if prime_list[i] and prime_list[N-i]:
            print('{} =  {} + {}'.format(N, i, N-i))
            break
    else:
        print('"Goldbach\'s conjecture is wrong."')