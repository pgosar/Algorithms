import java.util.*;

class Solution {
    public int solve(String a, String b) {
        int[][] ans = new int[a.length() + 1][b.length() + 1];
        for (int i = 0; i < a.length(); i++)  {
            for (int j = 0; j < b.length(); j++) {
                if (a.charAt(i) == b.charAt(j)) ans[i + 1][j + 1] = ans[i][j] + 1;
                else ans[i + 1][j + 1] = Math.max(ans[i][j + 1], ans[i + 1][j]);
            }
        }
        return ans[a.length()][b.length()];
    }
}
