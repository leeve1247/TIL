import sys
a = int(sys.stdin.readline().rstrip())
i = 0
while i < a:
    i += 1
    x, y = map(int, sys.stdin.readline().rstrip().split())
    print(x + y)