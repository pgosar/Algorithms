class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        def dfs(i, j, maxMove, memo):
            if (i, j, maxMove) in memo:
                return memo[(i, j, maxMove)]
            if maxMove < 0:
                return 0
            if i < 0 or i >= m or j < 0 or j >= n:
                return 1
            ans = 0
            ans += dfs(i-1,j,maxMove-1, memo)
            ans += dfs(i+1,j,maxMove-1, memo)
            ans += dfs(i,j-1,maxMove-1, memo)
            ans += dfs(i,j+1,maxMove-1, memo)
            memo[(i, j, maxMove)] = ans

            return memo[(i, j, maxMove)]
        return dfs(startRow, startColumn, maxMove, dict()) % 1000000007
