import sys
line = sys.stdin.readline().strip()
stack = []
prior = {
    '*':2,'/':2,'+':1,'-':1,'(':0
}
for w in '('+line+')':
    if 'A'<=w<='Z':
        print(w, end='')
    elif w == '(':
        stack.append(w)
    elif w == ')':
        while True:
            o = stack.pop()
            if o == '(':
                break
            print(o, end='')
    else:
        while stack[-1] != '(' and prior[w] <= prior[stack[-1]]:
            print(stack.pop(),end='')
        stack.append(w)