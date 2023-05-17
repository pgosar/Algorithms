import sys
input = sys.stdin.readline

n, m = map(int, input().split())
a = []
for _ in range(n):
    a.append(list(map(int, input().split())))
col = []
ans = 0

for i in range(n):
    good = False
    for j in range(m):
        if a[i][j] == 1:
            good = True
        elif good:
            ans += 1

for i in range(n):
    good = False
    for j in range(m-1, -1, -1):
        if a[i][j] == 1:
            good = True
        elif good:
            ans += 1

for j in range(m):
    good = False
    for i in range(n-1, -1, -1):
        if a[i][j] == 1:
            good = True
        elif good:
            ans += 1

for j in range(m):
    good = False
    for i in range(n):
        if a[i][j] == 1:
            good = True
        elif good:
            ans += 1

print(ans)
