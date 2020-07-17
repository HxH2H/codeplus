import sys
S = sys.stdin.readline().strip()
alpha = [-1]*26
for w in S:
    alpha[ord(w)-ord('a')] = S.index(w)
for j in alpha:
    print(j, end=' ')