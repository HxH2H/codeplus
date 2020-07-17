import sys
n = int(sys.stdin.readline())
n_arr = list(map(int, sys.stdin.readline().rstrip().split()))
result = [n_arr[i] for i in range(n)]
for i in range(1,n):
    for j in range(i):
        if n_arr[i] > n_arr[j] and result[i] < result[j] + n_arr[i]:
            result[i] = result[j] + n_arr[i]
print(max(result))