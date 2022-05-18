class Solution {
    public int numIslands(char[][] grid) {
        int count = 0;
        for (int i = 0; i < grid.length; i++) {
            for (int j = 0; j < grid[0].length; j++) {
                if (grid[i][j] == '1') {
                    helper(grid, i, j);
                    count++;
                }
            }
        }
        return count;
    }

    public void helper(char[][] matrix, int x, int y) {
        if (x >= 0 && y >= 0 && x < matrix.length && y < matrix[0].length && matrix[x][y] == '1') {
            matrix[x][y] = '0';
            helper(matrix, x + 1, y);
            helper(matrix, x - 1, y);
            helper(matrix, x, y + 1);
            helper(matrix, x, y - 1);
        }
    }
}
