import sys
n = int(sys.stdin.readline())
day_cost = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]
sum = 0 # 비용을 합 할 변수
def profit(day, s):
    global sum  # 전역 변수로 설정
    if day == n:    # n+1 (0으로 시작했으니 여기서는 n)일이 되면 종료
        sum = max(sum , s)  # 최대이익을 찾기
        return
    if day > n: # n+1을 넘기면 불가능
        return
    profit(day + 1, s)  # 해당 하는날에 상담을 안한 경우에는 다음날 상담 가능
    profit(day+day_cost[day][0], s + day_cost[day][1])  # 해당하는 날에 상담을 하였으면 다음날이 아닌 걸리는 날만큼 추가
profit(0, 0)
print(sum)