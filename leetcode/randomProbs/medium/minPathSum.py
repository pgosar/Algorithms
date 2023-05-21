class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        dp = grid.copy()
        m = len(grid)
        n = len(grid[0])
        for i in range(1, n):
            grid[0][i] += grid[0][i-1]
        for i in range(1, m):
            grid[i][0] += grid[i-1][0]
            
        for i in range(1,m):
            for j in range(1,n):
                dp[i][j] += min(dp[i-1][j], dp[i][j-1])
        return dp[-1][-1]
