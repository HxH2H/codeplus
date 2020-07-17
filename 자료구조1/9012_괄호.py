import sys
line = sys.stdin.readline().rstrip()
stack_1 = []
stack_2 = []
for w in line:
    stack_1.append(w)
n = int(sys.stdin.readline())
for _ in range(n):
    com = sys.stdin.readline().rstrip().split()
    if com[0] == 'L':
        if not stack_1:
            continue
        stack_2.append(stack_1.pop())
    if com[0] == 'D':
        if not stack_2:
            continue
        stack_1.append(stack_2.pop())
    if com[0] == 'B':
        if not stack_1:
            continue
        stack_1.pop()
    if com[0] == 'P':
        stack_1.append(com[1])
stack_2.reverse()
result = stack_1 + stack_2
for i in result:
    print(i, end='')

