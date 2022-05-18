import java.util.*;

class Solution {
    public int solve(String s) {
        int open = 0;
        int count = 0;
        for (char c : s.toCharArray()) {
            if (c == '(') open++;
            else if (open == 0) count++;
            else open--;
        }
        return count + open;
    }
}
