# 다음 순열의 코드를 일부 수정하여 사용
import sys
def prev_permutation(n_arr):
    i = len(n_arr) - 1
    while i > 0 and n_arr[i-1] <= n_arr[i]:
        i -= 1
    if i <= 0:
        return False
    j = len(n_arr) - 1
    while n_arr[i-1] <= n_arr[j]:
        j -= 1
    n_arr[i-1],n_arr[j] = n_arr[j],n_arr[i-1]
    j = len(n_arr) - 1
    while i < j:
        n_arr[i],n_arr[j] = n_arr[j],n_arr[i]
        i += 1
        j -= 1
    return True
n = int(sys.stdin.readline())
n_arr = list(map(int, sys.stdin.readline().rstrip().split()))
if prev_permutation(n_arr):
    print(' '.join(map(str, n_arr)))
else:
    print(-1)