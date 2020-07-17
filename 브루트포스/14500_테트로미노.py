import sys
n, m = map(int, sys.stdin.readline().rstrip().split())
paper = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]
result = 0
for i in range(n):
    for j in range(m):
        if j+3 < m:
            ans = paper[i][j] + paper[i][j+1] + paper[i][j+2] + paper[i][j+3]
            if result < ans: result = ans
        if i+3 < n:
            ans = paper[i][j] + paper[i+1][j] + paper[i+2][j] + paper[i+3][j]
            if result < ans: result = ans
        if j+1 < m and i+1 < n:
            ans = paper[i][j] + paper[i][j+1] + paper[i+1][j] + paper[i+1][j+1]
            if result < ans: result = ans
        if i+2 < n and j+1 < m:
            ans = paper[i][j] + paper[i+1][j] + paper[i+2][j] + paper[i+2][j+1]
            if result < ans: result = ans
        if i+2 < n and j-1 >= 0:
            ans = paper[i][j] + paper[i+1][j] + paper[i+2][j] + paper[i+2][j-1]
            if result < ans: result = ans
        if i+1 < n and j+2 < m:
            ans = paper[i][j] + paper[i+1][j] + paper[i+1][j+1] + paper[i+1][j+2]
            if result < ans: result = ans
        if i+1 < n and j-2 >= 0:
            ans = paper[i][j] + paper[i+1][j] + paper[i+1][j-1] + paper[i+1][j-2]
            if result < ans: result = ans
        if i+1 < n and j+2 < m:
            ans = paper[i][j] + paper[i][j+1] + paper[i][j+2] + paper[i+1][j+2]
            if result < ans: result = ans
        if i+1 < n and j+2 < m:
            ans = paper[i][j] + paper[i+1][j] + paper[i][j+1] + paper[i][j+2]
            if result < ans: result = ans
        if i+2 < n and j+1 < m:
            ans = paper[i][j] + paper[i][j+1] + paper[i+1][j] + paper[i+2][j]
            if result < ans: result = ans
        if i+2<n and j-1<m:
            ans = paper[i][j] + paper[i][j-1] + paper[i+1][j] + paper[i+2][j]
            if result < ans: result = ans
        if i+2<n and j+1<m:
            ans = paper[i][j] + paper[i+1][j] + paper[i+1][j+1] + paper[i+2][j+1]
            if result < ans: result = ans
        if i+2<n and j-1 >= 0:
            ans = paper[i][j] + paper[i+1][j] + paper[i+1][j-1] + paper[i+2][j-1]
            if result < ans: result = ans
        if i+1<n and j-2 >=0:
            ans = paper[i][j] + paper[i][j-1] + paper[i+1][j-1] + paper[i+1][j-2]
            if result < ans: result = ans
        if i+1<n and j+2<m:
            ans = paper[i][j] + paper[i][j+1] + paper[i+1][j+1] + paper[i+1][j+2]
            if result < ans: result = ans
        if j+2<m:
            ans = paper[i][j] + paper[i][j+1] + paper[i][j+2]
            if i-1 >= 0:
                ans2 = ans + paper[i-1][j+1]
                if result < ans2: result = ans2
            if i+1 < n:
                ans2 = ans + paper[i+1][j+1]
                if result < ans2: result = ans2
        if i+2<n:
            ans = paper[i][j] + paper[i+1][j] + paper[i+2][j]
            if j+1 < m:
                ans2 = ans + paper[i+1][j+1]
                if result < ans2: result = ans2
            if j-1 >= 0:
                ans2 = ans + paper[i+1][j-1]
                if result < ans2: result = ans2
print(result)