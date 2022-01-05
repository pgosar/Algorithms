import java.util.*;

class Solution {
    public int solve(int[][] matrix) {
        int count = 0;
        for (int i = 0; i < matrix.length; i++) {
            for (int j = 0; j < matrix[0].length; j++) {
                if (matrix[i][j] == 1) {
                    helper(matrix, i, j);
                    count++;
                }
            }
        }
        return count;
    }

    public void helper(int[][] matrix, int x, int y) {
        if (x >= 0 && y >= 0 && x < matrix.length && y < matrix[0].length && matrix[x][y] == 1) {
            matrix[x][y] = 0;
            helper(matrix, x + 1, y);
            helper(matrix, x - 1, y);
            helper(matrix, x, y + 1);
            helper(matrix, x, y - 1);
        }
    }
}
