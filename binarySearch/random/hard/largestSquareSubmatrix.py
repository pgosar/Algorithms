class Solution:
    def solve(self, matrix):
        dp = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
        ans = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 1:
                    dp[i][j] = min(dp[i][j - 1], dp[i - 1][j - 1], dp[i - 1][j]) + 1
            ans = max(ans, max(dp[i]))
        return ans * ans
