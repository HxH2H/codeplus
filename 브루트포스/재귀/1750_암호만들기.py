import sys
def check(password):        # 자음과 모음의 갯수 파악 자음이 최소 2개 모음은 1개
    ja = 0
    mo = 0
    for x in password:
        if x in 'aeiou':
            mo += 1
        else:
            ja += 1
    return ja >= 2 and mo >= 1
def secret(n, al, password, index):
    if len(password) == n:  # 암호의 길이가 제한된 길이와 같다면
        if check(password): # 자음과 모음의 갯수를 파악하여 암호를 출력한다.
            print(password)
        return      # 잊지 말것!@#!@#!@#!@#!@#!@#!@#!@#
    if index >= len(al):    # 사용가능한 알파벳의 갯수에서 벗어나면 불가능
        return
    secret(l, al, password + al[index], index+1)    # 해당 알파벳을 사용했을 경우의 재귀 항상 이게 먼저 와야 한다.
    secret(l, al, password, index+1)                # 해당 알파벳을 사용하지 않았을 경우의 재귀
    return      # 잊지 말것 @@@@@@@!!!@!@!@#!@#!@#
l,c = map(int, sys.stdin.readline().rstrip().split())
alpha = sys.stdin.readline().rstrip().split()
alpha.sort()    # 암호는 증가하는 순서로 구성되어 있다.
secret(l, alpha, "", 0) # 암호의 길이, 사용가능한 알파벳, 완성된 암호, 사용 여부