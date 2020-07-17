import sys
chanel = int(sys.stdin.readline())
n = int(sys.stdin.readline())
broken_cha = [False] * 10
if n == 0:
    broken = []
else:
    broken = list(map(int, sys.stdin.readline().rstrip().split()))
for x in broken:
    broken_cha[x] = True
def pos(c):
    if c == 0:
        if broken_cha[c]:
            return 0
        else:
            return 1
    l = 0
    while c > 0:
        if broken_cha[c%10]:
            return 0
        l += 1
        c //= 10
    return l
result = abs(chanel-100)
for i in range(1000001):
    move_cha = i
    l = pos(move_cha)
    if l > 0:
        press = abs(move_cha - chanel)
        if result > l + press:
            result = l+press
print(result)