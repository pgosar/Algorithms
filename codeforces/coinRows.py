import sys
input = sys.stdin.readline

for _ in range(int(input())):
    m = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    s1, s2 = sum(a), 0
    ans = float('inf')
    for i in range(m):
        s1 -= a[i]
        ans = min(ans, max(s1, s2))
        s2 += b[i]
    print(ans)
        

