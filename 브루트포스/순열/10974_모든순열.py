# 다음 순열이 코드를 활용
import sys
def permutation(n):
    i = n - 1
    while i > 0 and n_arr[i-1] >= n_arr[i]:
        i -= 1
    if i <= 0:
        return False
    j = n - 1
    while n_arr[j] <= n_arr[i-1]:
        j -= 1
    n_arr[i-1], n_arr[j] = n_arr[j], n_arr[i-1]
    j = n - 1
    while i < j:
        n_arr[i],n_arr[j] = n_arr[j],n_arr[i]
        i += 1
        j -= 1
    return True
n = int(sys.stdin.readline())
n_arr = list(range(1, n+1))
while True:
    print(' '.join(map(str, n_arr)))
    if not permutation(n):
        break
