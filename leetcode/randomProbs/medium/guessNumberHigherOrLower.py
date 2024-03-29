class Solution:
    def getMoneyAmount(self, n: int) -> int:
        dp = [[0] * (n+1) for _ in range(n+1)]
        for i in range(n, 0, -1):
            for j in range(i+1,n+1):
                dp[i][j] = float('inf')
                for k in range(i, j):
                    dp[i][j] = min(dp[i][j], max(dp[i][k-1] + k, dp[k+1][j] + k))
        print(dp)
        return dp[1][-1]
