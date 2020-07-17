import sys
blocks = (
    ((0,1), (0,2), (0,3)),
    ((1,0), (2,0), (3,0)),
    ((1,0), (1,1), (1,2)),
    ((0,1), (1,0), (2,0)),
    ((0,1), (0,2), (1,2)),
    ((1,0), (2,0), (2,-1)),
    ((0,1), (0,2), (-1,2)),
    ((1,0), (2,0), (2,1)),
    ((0,1), (0,2), (1,0)),
    ((0,1), (1,1), (2,1)),
    ((0,1), (1,0), (1,1)),
    ((0,1), (-1,1), (-1,2)),
    ((1,0), (1,1), (2,1)),
    ((0,1), (1,1), (1,2)),
    ((1,0), (1,-1), (2,-1)),
    ((0,1), (0,2), (-1,1)),
    ((0,1), (0,2), (1,1)),
    ((1,0), (2,0), (1,1)),
    ((1,0), (2,0), (1,-1))
)
n, m  = map(int, sys.stdin.readline().rstrip().split())
paper = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]
result = 0
for i in range(n):
    for j in range(m):
        for block in blocks:
            is_true = True
            ans = paper[i][j]
            for dx, dy in block:
                x, y = i+dx, j+dy
                if 0 <= x < n and 0 <= y < m:
                    ans += paper[x][y]
                else:
                    is_true = False
                    break
            if is_true and result < ans:
                result = ans
print(result)