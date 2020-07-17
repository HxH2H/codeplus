import sys
while True:
    line = sys.stdin.readline().rstrip('\n')
    lo,up,nm,sp = 0,0,0,0
    if not line:
        break
    for w in line:
        if w.isupper():
            up += 1
        elif w.islower():
            lo += 1
        elif w.isdigit():
            nm += 1
        elif w.isspace():
            sp += 1
    print('{} {} {} {}'.format(lo, up, nm, sp))