import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n, m = map(int, input().split())
    a = sorted(list(map(int, input().split())), reverse=True)
    b = list(map(int, input().split()))
    ans, j = 0, 0
    for i in a:
        ans += b[min(j, i-1)]
        j += 1
    print(ans)
