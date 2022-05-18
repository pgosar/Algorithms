import java.util.*;

class Solution {
    public int solve(int[][] matrix) {
        int[][] ans = new int[matrix.length][matrix[0].length];
        ans[0][0] = matrix[0][0];
        for (int i = 0; i < matrix.length; i++) {
            for (int j = 0; j < matrix[0].length; j++) {
                if (i > 0) ans[i][j] = Math.max(ans[i - 1][j] + matrix[i][j], ans[i][j]);
                if (j > 0) ans[i][j] = Math.max(ans[i][j - 1] + matrix[i][j], ans[i][j]);
            }
        }
        return ans[matrix.length - 1][matrix[0].length - 1];
    }
}
