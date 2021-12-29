import java.util.*;

class Solution {
    public int solve(int[][] matrix) {
        int row = matrix.length;
        int col = matrix[0].length;
        int max = 0;
        boolean[][] visited = new boolean[row][col];
        for (int i = 0; i < row; i++) {
            for (int j = 0; j < col; j++) {
                max = Math.max(max, helper(matrix, i, j, visited));
            }
        }
        return max;
    }

    private int helper(int[][] matrix, int i, int j, boolean[][] visited) {
        if (i < 0 || j < 0 || i >= matrix.length || 
            j >= matrix[0].length || visited[i][j] || matrix[i][j] == 0) 
            return 0; 

        int area = 1;
        visited[i][j] = true;
        area += helper(matrix, i + 1, j, visited);
        area += helper(matrix, i - 1, j, visited);
        area += helper(matrix, i, j + 1, visited);
        area += helper(matrix, i, j - 1, visited);
        return area;
    }
}
