import sys
line = sys.stdin.readline().strip()
li = []
for _ in range(len(line)):
    li.append(line)
    line = line[1:]
li.sort()
for i in li:
    print(i)