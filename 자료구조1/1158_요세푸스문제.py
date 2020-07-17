import sys
from collections import deque
n, k = map(int, sys.stdin.readline().rstrip().split())
queue = deque([i for i in range(1, n+1)])
result = '<'
while queue:
    if len(queue) == 1:
        result += str(queue.pop())
        break
    for _ in range(k):
        queue.append(queue.popleft())
    result += str(queue.pop())
    result += ', '
result += '>'
print(result)