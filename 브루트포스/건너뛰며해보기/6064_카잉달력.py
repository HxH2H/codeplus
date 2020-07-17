# 빠른 연산을 위해서는 나머지연산을 이용한다.
import sys
t = int(sys.stdin.readline())
for _ in range(t):
    m,n,x,y = map(int, sys.stdin.readline().rstrip().split())
    x -= 1  # 나머지연산을 위해 1을 빼준다.
    y -= 1  # 마찬가지
    i = x
    while i < m*n:
        if i%n == y:    # x를 고정시켰으니 n을 이용하여 나머지연산하여 y의 값을 구한다.
            print(i+1)
            break
        i += m      # m만큼 증가시켜 x의 값을 고정
    else:
        print(-1)