import java.util.*;

class Solution {
    public int solve(int[][] matrix) {
        int perimeter = 0;
        for (int x = 0; x < matrix.length; x++) {
            for (int y = 0; y < matrix[0].length; y++) {
                perimeter += helper(matrix, x, y);
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
