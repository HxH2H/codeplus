import sys
height = [int(sys.stdin.readline()) for _ in range(9)]
ans = sum(height)
height.sort()
for i in range(9):
    for j in range(i+1, 9):
        if ans - height[i] - height[j] == 100:
            for l in range(9):
                if height[l] == height[i] or height[l] == height[j]:
                    continue
                print(height[l])
            sys.exit(0) # 정답이 여러개일 때 하나만 출력하고 끝내고 싶다면 이 명령어를 입력해줘야 한다.