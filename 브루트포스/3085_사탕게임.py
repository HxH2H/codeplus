import sys
n = int(sys.stdin.readline())
candy = [list(sys.stdin.readline().rstrip()) for _ in range(n)]
result = 0
def check(a):
    ans = 1
    for i in range(n):
        count = 1
        for j in range(1, n):       # 왼쪽과 사탕의 색이 같은지를 비교
            if a[i][j] == a[i][j-1]:    # 같은 색이라면 먹을 수 있는 사탕의 갯수를 올려준다
                count += 1
            else:
                count = 1
            if ans < count:
                ans = count
        count = 1
        for j in range(1, n):
            if a[j][i] == a[j-1][i]:
                count += 1
            else:
                count = 1
            if ans < count:
                ans = count
    return ans
for i in range(n):
    for j in range(n):
        if j+1 < n:     # 오른쪽에 있는 사탕과 자리 교환 (열)
            candy[i][j], candy[i][j+1] = candy[i][j+1], candy[i][j]
            ans = check(candy)
            if result < ans:
                result = ans
            candy[i][j], candy[i][j+1] = candy[i][j+1], candy[i][j]
        if i+1 < n:     # 아래쪽에 있는 사탕과 자리 교환 (행)
            candy[i][j], candy[i+1][j] = candy[i+1][j], candy[i][j]
            ans = check(candy)
            if result < ans:
                result = ans
            candy[i][j], candy[i+1][j] = candy[i+1][j], candy[i][j]
print(result)