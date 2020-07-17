import sys
n = int(sys.stdin.readline())
n_arr = list(map(int, sys.stdin.readline().rstrip().split()))
result = [1]*n
for i in range(n-1, -1, -1):
    for j in range(n-1,i,-1):
        if n_arr[i] > n_arr[j] and result[i] < result[j] + 1:
            result[i] = result[j] + 1
print(max(result))

# import sys
# n = int(sys.stdin.readline())
# n_arr = list(map(int, sys.stdin.readline().rstrip().split()))
# result = [1] * n
# n_arr.reverse()
# for i in range(1, n):
#     for j in range(i):
#         if n_arr[i] > n_arr[j] and result[i] < result[j] + 1:
#             result[i] = result[j] + 1
# print(max(result))