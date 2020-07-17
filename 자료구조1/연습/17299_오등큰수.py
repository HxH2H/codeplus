import sys
n = int(sys.stdin.readline())
num = list(map(int, sys.stdin.readline().rstrip().split()))
stack = [0]
ans = [0]*n
freq = [0]*(n+1)
for i in num:
    freq[i] += 1
for i in range(1, n):
    while stack and freq[num[stack[-1]]] < freq[num[i]]:
        ans[stack[-1]] = num[i]
        stack.pop()
    stack.append(i)
while stack:
    ans[stack.pop()] = -1
for i in ans:
    print(i, end=' ')