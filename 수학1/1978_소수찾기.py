import sys
def prime(x):
    st_n = 2
    if x < 2:
        return False
    while st_n**2 <= x:
        if x % st_n == 0:
            return False
        st_n += 1
    return True
n = int(sys.stdin.readline())
num = list(map(int,sys.stdin.readline().rstrip().split()))
count = 0
for i in range(n):
    if prime(num[i]) == True:
        count += 1
print(count)