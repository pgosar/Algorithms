class Solution:
    def orderOfLargestPlusSign(self, n: int, mines: List[List[int]]) -> int:
        grid = [[n] * n for _ in range(n)]
        for i, j in mines:
            grid[i][j] = 0
        for i in range(n):
            l = r = u = d = 0
            for j, k in zip(range(n), reversed(range(n))):
                l = l + 1 if grid[i][j] != 0 else 0
                grid[i][j] = min(grid[i][j], l)

                r = r + 1 if grid[i][k] != 0 else 0
                grid[i][k] = min(grid[i][k], r)

                u = u + 1 if grid[j][i] != 0 else 0
                grid[j][i] = min(grid[j][i], u)

                d = d + 1 if grid[k][i] != 0 else 0
                grid[k][i] = min(grid[k][i], d)

        return max(max(row) for row in grid)
