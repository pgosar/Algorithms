import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    s = input().strip()
    dp = [0] * n
    for i in range(n-1, -1, -1):
        dp[i] += 1 if s[i] == 'W' else -1
        if i > 0:
            dp[a[i-1]-1] += dp[i]
    print(dp.count(0))
