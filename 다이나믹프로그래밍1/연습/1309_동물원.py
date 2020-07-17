import sys
n = int(sys.stdin.readline())
cage = [[0]*3 for _ in range(n)]
for i in range(n):
    if i == 0:
        cage[i][0] = 1
        cage[i][1] = 1
        cage[i][2] = 1
    else:
        cage[i][0] = (cage[i-1][0] + cage[i-1][1] + cage[i-1][2]) % 9901
        cage[i][1] = (cage[i-1][0] + cage[i-1][2]) % 9901
        cage[i][2] = (cage[i-1][0] + cage[i-1][1]) % 9901
print(sum(cage[n-1]) % 9901)
# cage[0][0] = 1
#