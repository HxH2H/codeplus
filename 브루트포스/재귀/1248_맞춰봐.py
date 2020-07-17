import sys
def check(index):
    s = 0
    for i in range(index, -1, -1):  # 정답 수열을 뒤에서부터 합하면서 주어진 부호에 해당하는지 확인해준다.
        s += ans[i]
        if sign[i][index] == 0:
            if s != 0:
                return False
        elif sign[i][index] < 0:
            if s >= 0:
                return False
        elif sign[i][index] > 0:
            if s <= 0:
                return False
    return True
def find(index):
    if index == n:  # 수열의 크기 만큼 도달 했으면 끝
        return True
    if sign[index][index] == 0: # [i,i]가 0 이면 0밖에 없으므로 0을 정답에 삽입
        ans[index] = 0
        return check(index) and find(index+1)   # 재귀
    for i in range(1, 11):
        ans[index] = i * sign[index][index]
        if check(index) and find(index+1):
            return True
    return False
n = int(sys.stdin.readline())   # 수열의 크기
s = sys.stdin.readline().rstrip()   # 주어지는 문자열
sign = [[0]*n for _ in range(n)]    # 문자열을 넣기 위한 2차원 리스트
ans =[0]*n      # 정답 수열을 저장하는 리스트
cnt = 0
for i in range(n):      # 주어진 문자열의 기호를 파악하여 알맞는 위치에 넣어준다
    for j in range(i, n):
        if s[cnt] == '0':
            sign[i][j] = 0
        elif s[cnt] == '+':
            sign[i][j] = 1
        else:
            sign[i][j] = -1
        cnt += 1
find(0)
print(' '.join(map(str, ans)))