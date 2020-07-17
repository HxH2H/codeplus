import sys
def GCD(a, b):
    if b == 0:
        return a
    return GCD(b, a%b)
def LCM(a, b):
    return ((a*b) // GCD(a,b))

a, b = map(int, sys.stdin.readline().strip().split())
print(GCD(a,b))
print(LCM(a,b))