import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n, m, k = map(int, input().split())
    a = list(map(int, input().split()))
    i = 0
    pos = True
    for i in range(n - 1):
        m += min(a[i] - (a[i+1] - k), a[i])
        pos = pos and m >= 0
    print("YES" if pos else "NO")
