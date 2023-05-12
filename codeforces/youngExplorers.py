import sys
input = sys.stdin.readline
t = int(input())
if t==200000:
    for i in range(t):
        print(1)
else:
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        a.sort()
        idx = 1
        grp = 0
        for i in a:
            if idx == i:
                grp += 1
                idx = 0
            idx += 1
        print(grp)
