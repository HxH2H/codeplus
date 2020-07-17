import sys
line = sys.stdin.readline().rstrip()
stack = []
result = 0
for w in range(len(line)):
    if line[w] == '(':
        stack.append(w)
    if line[w] == ')':
        if w - stack[-1] == 1:
            stack.pop()
            result += len(stack)
        else:
            stack.pop()
            result += 1
print(result)