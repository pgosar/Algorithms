class Solution {
    public int islandPerimeter(int[][] grid) {
        int perimeter = 0;
        for (int i = 0; i < grid.length; i++) {
            for (int j = 0; j < grid[0].length; j++) {
                perimeter += helper(matrix, i, j);
            }
        }
        return perimeter;
    }
    
    public int helper(int[][] matrix, int x, int y) {
        int count = 0;
        if (matrix[x][y] == 1) {
            count = 4;
            if (x < matrix.length - 1 && matrix[x + 1][y] == 1) count--;
            if (x > 0 && matrix[x - 1][y] == 1) count--;
            if (y < matrix[0].length - 1 && matrix[x][y + 1] == 1) count--;
            if (y > 0 && matrix[x][y - 1] == 1) count--;
        }
        return count;
    }
}
