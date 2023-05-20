import sys
input = sys.stdin.readline
for _ in range(int(input())):
    n, k = map(int, input().split())
    a = sorted(list(map(int, input().split())))
    l, r = 0, len(a)-1
    ans = 0
    for i in range(k):
        ans += a[n-1-i-k]//a[n-1-i]
    ans += sum(a[0:n-2*k])
    print(ans)
