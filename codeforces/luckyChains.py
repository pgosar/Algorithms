from math import *
import sys
input = sys.stdin.readline
m = 10**7+1
dp = [0]*m
for i in range(2, m):
    if dp[i] == 0:
        for j in range(i, m, i):
            dp[j] = i
for _ in range(int(input())):
    a, b = map(int, input().split())
    if gcd(a, b) != 1:
        print(0)
    elif abs(b-a) == 1:
        print(-1)
    elif abs(b-a) % 2 == 0:
        print(1)
    else:
        x = b-a
        ans = x-a % x
        while x != 1:
            ans = min(ans, dp[x] - a % dp[x])
            x //= dp[x]
        print(ans)
