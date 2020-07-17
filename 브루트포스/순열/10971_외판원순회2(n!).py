import sys
def permutation(n): # 외판원이 갈 수 있는 모든 경로르 탐색
    i = n-1
    while i > 0 and ob[i-1] >= ob[i]:
        i -= 1
    if i <= 0:
        return False
    j = n-1
    while ob[i-1] >= ob[j]:
        j -= 1
    ob[i-1],ob[j] = ob[j],ob[i-1]
    j = n-1
    while i<j:
        ob[i],ob[j] = ob[j],ob[i]
        i+=1
        j-=1
    return True
n = int(sys.stdin.readline())
cost = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]
ob = list(range(n))
ans = 2147483647
while True:
    is_true = True  # 비용이 0인지 아닌지 판별하기 위한 변수
    result = 0
    for i in range(0, n-1):
        if cost[ob[i]][ob[i+1]] == 0:   # 갈 수 없는 방법
            is_true = False
        else:
            result += cost[ob[i]][ob[i+1]]  # 갈 수 있는 곳이면 비용을 합한다.
    if is_true and cost[ob[-1]][ob[0]] != 0:    # 원점으로 도착할 때의 비용이 0이 아닌 경우
        result += cost[ob[-1]][ob[0]]
        ans = min(ans, result)
    if not permutation(n):
        break
    if ob[0] != 0:  # 가장 처음에 존재하는 수가 0이 아니면 할 필요가 없기 때문에 break
        break
print(ans)