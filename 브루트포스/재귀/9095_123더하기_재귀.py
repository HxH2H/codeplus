import sys
def plus(s, goal):
    if s > goal:
        return 0
    if s == goal:
        return 1
    count = 0
    for i in range(1, 4):
        count += plus(s+i, goal)
    return count
t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    print(plus(0, n))