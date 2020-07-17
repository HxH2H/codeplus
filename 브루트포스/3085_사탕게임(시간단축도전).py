# 바뀐 자리로 인해 영향을 받는 행과 열에 대해서만 연산을 해주면 된다.
import sys
n = int(sys.stdin.readline())
candy = [list(sys.stdin.readline().rstrip()) for _ in range(n)]
result = 0
def check(x,y,dx,dy):
    ans = 1
    max_ans = 0
    for i in range(n-1):
        nx, ny = x + dx, y + dy
        if candy[x][y] == candy[nx][ny]:
            ans += 1
            max_ans = max(max_ans, ans)
        else:
            ans = 1
        x, y = nx, ny
    return max_ans
for i in range(n):
    for j in range(n-1):
        # 오른쪽 열과 교환
        candy[i][j], candy[i][j+1] = candy[i][j+1], candy[i][j]
        result = max(result, check(i, 0, 0, 1), check(0, j, 1, 0), check(0, j+1, 1, 0))
        candy[i][j], candy[i][j+1] = candy[i][j+1], candy[i][j]
        # 아래 행과 교환
        candy[j][i], candy[j+1][i] = candy[j+1][i], candy[j][i]
        result = max(result, check(0, i, 1, 0), check(j, 0, 0, 1), check(j+1, 0, 0, 1))
        candy[j][i], candy[j+1][i] = candy[j+1][i], candy[j][i]
print(result)