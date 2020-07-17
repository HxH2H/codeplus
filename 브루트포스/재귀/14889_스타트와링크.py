import sys
def soccer(index, first, second):
    if index == n:              # 모든 인덱스를 통과하여 두 팀으로 나누었을 때
        if len(first) != n//2:      # 첫번째 팀의 수가 총 인원의 반이 아닐 경우 -1을 반환
            return -1
        if len(second) != n//2:     # 두번째 팀도 마찬가지
            return -1
        t1 = 0
        t2 = 0
        for i in range(n//2):
            for j in range(n//2):
                if i == j:
                    continue
                t1 += S[first[i]][first[j]]
                t2 += S[second[i]][second[j]]
        balance = abs(t1 - t2)
        return balance
    if len(first) > n//2:
        return -1
    if len(second) > n//2:
        return -1
    ans = -1
    t1 = soccer(index+1, first+[index], second)
    if ans == -1 or (t1 != -1 and ans > t1):
        ans = t1
    t2 = soccer(index+1, first, second + [index])
    if ans == -1 or (t2 != -1 and ans > t2):
        ans = t2
    return ans
n = int(sys.stdin.readline())
S = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]
print(soccer(0, [], []))