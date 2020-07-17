import sys
def next_permutation(n):
    i = n - 1
    while i > 0 and n_arr[i-1] >= n_arr[i]:
        i -= 1
    if i <= 0:
        return False
    j = n-1
    while n_arr[j] <= n_arr[i-1]:
        j -= 1
    n_arr[i-1],n_arr[j] = n_arr[j],n_arr[i-1]
    j = n-1
    while i < j:
        n_arr[i],n_arr[j] = n_arr[j],n_arr[i]
        i += 1
        j -= 1
    return True
def calc(n):
    ans = 0
    for i in range(1, n):
        ans += abs(n_arr[i-1] - n_arr[i])
    return ans
n = int(sys.stdin.readline())
n_arr = list(map(int, sys.stdin.readline().rstrip().split()))
n_arr.sort()
ans = 0
while True:
    result = calc(n)
    ans = max(result, ans)
    if not next_permutation(n):
        break
print(ans)