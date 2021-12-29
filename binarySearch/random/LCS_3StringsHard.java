import java.util.*;

class Solution {
    public int solve(String a, String b, String c) {
        int[][][] sol = new int[a.length() + 1][b.length() + 1][c.length() + 1];
        for (int i=0; i<= a.length(); i++) {
            for (int j=0; j<= b.length(); j++) {
                for (int k=0; k<= c.length(); k++) {
                    if (i == 0 || j == 0||k==0)
                        sol[i][j][k] = 0;
                    else if (a.charAt(i - 1) == b.charAt(j - 1)
                                && a.charAt(i - 1) == c.charAt(k - 1))
                        sol[i][j][k] = sol[i-1][j-1][k-1] + 1;
                    else
                        sol[i][j][k] = Math.max(Math.max(sol[i-1][j][k],
                                             sol[i][j-1][k]),
                            sol[i][j][k-1]);
                }
            }
        }
        return sol[a.length()][b.length()][c.length()];
    }
}
