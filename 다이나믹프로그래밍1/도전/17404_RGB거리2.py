# 1번 집의 색은 2번과 N번 집의 색과 같지 않아야 한다.
# 이 말은 즉, 원형의 모양을 지닌 집의 모임이다.
# 이 문제는 먼저 직선인 경우일 떄를 먼저 짜고
# 후에 원형의 조건을 추가해준다.
import sys
n = int(sys.stdin.readline())
result = [[0]*3 for _ in range(n+1)]    # 최솟값을 저장할 리스트
house =[[0,0,0]] + [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]    # 색의 비용
ans = 1000*1000 + 1
for k in range(3):              # 1번 집의 지붕 색 고정
    for j in range(3):
        if j == k:
            result[1][j] = house[1][j]
        else:
            result[1][j] = 1000*1000 + 1    # 1번 집의 지붕색을 고정했으니 그 외에는 그냥 큰값을 넣어준다 (계산 방해 금지)
    for i in range(2, n+1):   # 1번 집의 색을 고정했기 때문에 2번 집부터 시작
        result[i][0] = min(result[i-1][1], result[i-1][2]) + house[i][0]
        result[i][1] = min(result[i-1][0], result[i-1][2]) + house[i][1]
        result[i][2] = min(result[i-1][0], result[i-1][1]) + house[i][2]
    for l in range(3):  # n번 집의 색
        if l == k:      # 1번 집의 색인 경우 건너뛴다.
            continue
        ans = min(ans, result[n][l])    # 그 외의 색의 사용한 값을 비교하여 가장 작은 값이 정답
print(ans)