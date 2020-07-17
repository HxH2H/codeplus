import sys
def check(index):
    a = 0
    for i in range(index, -1, -1):
        a += ans[i]
        if sign[i][index] == 0:
            if a != 0:
                return False
        elif sign[i][index] > 0:
            if a <= 0:
                return False
        elif sign[i][index] < 0:
            if a >= 0:
                return False
    return True
def find(index):
    if index == n:
        return True
    if sign[index][index] == 0:
        ans[index] = 0
        return check(index) and find(index+1)
    for i in range(1, 11):
        ans[index] = i * sign[index][index]
        if check(index) and find(index+1):
            return True
    return False

n = int(sys.stdin.readline())
s = sys.stdin.readline().rstrip()
sign = [[0]*n for _ in range(n)]
ans = [0]*n
cnt = 0
for i in range(n):
    for j in range(i, n):
        if s[cnt] == '0':
            sign[i][j] = 0
        elif s[cnt] == '+':
            sign[i][j] = 1
        else:
            sign[i][j] = -1
        cnt += 1
find(0)
print(' '.join(map(str, ans)))