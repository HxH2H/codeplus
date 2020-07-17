import sys
line = sys.stdin.readline().rstrip()
stack = []
result = ''
tag = False
for w in line:
    if w == '<':
        while stack:
            result += stack.pop()
        tag = True
        result += '<'
    elif w == '>':
        result += '>'
        tag = False
    elif tag == True:
        result += w
    else:
        if w == ' ':
            while stack:
                result += stack.pop()
            result += ' '
        else:
            stack.append(w)
while stack:
    result += stack.pop()
print(result)