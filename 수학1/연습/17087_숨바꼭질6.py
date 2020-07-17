import sys
def GCD(a, b):
    if b == 0:
        return a
    return GCD(b, a%b)
N, S = map(int, sys.stdin.readline().rstrip().split())
s_loc = list(map(int,sys.stdin.readline().rstrip().split()))
max_gcd = 0
num = 0
for i in range(N):
    if s_loc[i] < S:
        s_loc[i] = S - s_loc[i]
    if s_loc[i] > S:
        s_loc[i] = s_loc[i] - S
if len(s_loc) == 1:
    print(s_loc[0])
else:
    while num != N:
        max_gcd = GCD(s_loc[num], max_gcd)
        num += 1
    print(max_gcd)