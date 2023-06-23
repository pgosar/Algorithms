class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        r, c = query_row, query_glass
        dp = [[0 for _ in range(x)] for x in range(1, r+2)]
        dp[0][0] = poured
        for i in range(r):
            for j in range(len(dp[i])):
                tmp = (dp[i][j] -1) /2
                if tmp > 0:
                    dp[i+1][j] += tmp
                    dp[i+1][j+1] += tmp
        return min(dp[r][c], 1)
