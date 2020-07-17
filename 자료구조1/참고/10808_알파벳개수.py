import sys
S = sys.stdin.readline().strip()
alpha = [0]*26
for w in S:
    alpha[ord(w)-ord('a')] += 1
for i in alpha:
    print(i, end=' ')