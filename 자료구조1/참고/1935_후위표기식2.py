import sys
n = int(sys.stdin.readline())
line = sys.stdin.readline().strip()
stack = []
alpha = [0]*n
for i in range(n):
    alpha[i] = int(sys.stdin.readline())
for w in line:
    if 'A'<=w<='Z':
        num = alpha[ord(w)-ord('A')]
        stack.append(num)
    else:
        b = stack.pop()
        a = stack.pop()
        if w == '+':
            stack.append(a+b)
        elif w == '-':
            stack.append(a-b)
        elif w == '*':
            stack.append(a*b)
        elif w == '/':
            stack.append(a/b)
print('{:.2f}'.format(stack[0]))