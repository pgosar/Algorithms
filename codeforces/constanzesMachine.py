import sys
input = sys.stdin.readline
M = 10 ** 9 + 7
s = input().strip()
if 'm' in s or 'w' in s:
    print(0)
else:
    dp = [1, 1] + [0] * (len(s) -1)
    for i in range(2, len(s)+1):
        if(s[i-1] == s[i-2] and (s[i-1] == 'u' or s[i-1] == 'n')):
            dp[i] = dp[i-1]+dp[i-2]%M
        else:
            dp[i] = (dp[i-1]%M)
    print(dp[-1] % M)
