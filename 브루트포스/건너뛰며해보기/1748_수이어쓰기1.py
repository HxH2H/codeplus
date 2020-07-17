import sys
n = int(sys.stdin.readline())
start = 1
result = 0
length = 1
while start <= n:
    end = start * 10 - 1
    if end > n:
        end = n
    result += (end - start + 1) * length
    start *= 10
    length += 1
print(result)