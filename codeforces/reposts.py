import sys
input = sys.stdin.readline

n = int(input())
d = {"polycarp":1}
for i in range(n):
    a, b, c = input().split()
    d[a.lower()] = d[c.lower()] + 1
print(max(d.values()))
