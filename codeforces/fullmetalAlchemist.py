def lcs(str1, str2):
    m = len(str1)
    n = len(str2)
    dp = [[0] * (n + 2) for _ in range(m + 2)]
    for i in range(m + 1):
        for j in range(n + 1):
            if (i == 0):
                dp[i][j] = j
            elif (j == 0):
                dp[i][j] = i
            elif (str1[i - 1] == str2[j - 1]):
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                dp[i][j] = min(dp[i - 1][j],
                               dp[i][j - 1]) + 1

    return dp[m][n]

if int(input()) == 1:
    print(len(input()))
else:
    print(lcs(input(), input()))
