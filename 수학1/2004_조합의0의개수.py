import sys
def two(x):
    ans = 0
    while x != 0:
        x = x // 2
        ans += x
    return ans
def five(x):
    ans = 0
    while x != 0:
        x = x // 5
        ans += x
    return ans
n, m = map(int, sys.stdin.readline().rstrip().split())
print(min(two(n)-two(n-m)-two(m), five(n)-five(n-m)-five(m)))