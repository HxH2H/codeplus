import sys
t = int(sys.stdin.readline())
for _ in range(t):
    stack = []
    result = ''
    line = sys.stdin.readline().rstrip()
    for word in line:
        if word == ' ':
            while stack:
                result += stack.pop()
            result += ' '
        else:
            stack.append(word)
    while stack:
        result += stack.pop()
    print(result)