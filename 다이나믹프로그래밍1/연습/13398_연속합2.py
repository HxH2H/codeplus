import sys
n = int(sys.stdin.readline())
n_arr = list(map(int, sys.stdin.readline().rstrip().split()))
u_arr = [0]*n
d_arr = [0]*n
for i in range(n):
    u_arr[i] = n_arr[i]
    if i == 0:
        continue
    if u_arr[i] < u_arr[i-1] + n_arr[i]:
        u_arr[i] = u_arr[i-1] + n_arr[i]
for i in range(n-1,-1,-1):
    d_arr[i] = n_arr[i]
    if i == n-1:
        continue
    if d_arr[i] < d_arr[i+1] + n_arr[i]:
        d_arr[i] = d_arr[i+1] + n_arr[i]
ans = max(u_arr)
for i in range(1, n-1):
    if ans < u_arr[i-1] + d_arr[i+1]:
        ans = u_arr[i-1] + d_arr[i+1]
print(ans)