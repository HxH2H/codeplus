import sys
def good(prev, choice, eq): # 부등호의 식이 성립하는지 확인하는 함수
    if eq == '<':
        if prev > choice:
            return False
    if eq == '>':
        if prev < choice:
            return False
    return True
def find(index, s):
    if index == n+1:
        result.append(s)
        return
    for i in range(10):
        if check[i]:
            continue
        if index == 0 or good(s[index-1], str(i), a[index-1]):
            check[i] = True
            find(index+1, s+str(i))
            check[i] = False

n = int(sys.stdin.readline())
a = sys.stdin.readline().rstrip().split()
check = [False]*10      # 숫자가 중복되지 않게 사용했는지 여부를 파악
result = []             # 선택된 숫자를 저장할 공간
find(0, '')
result.sort()
print(result[-1])
print(result[0])