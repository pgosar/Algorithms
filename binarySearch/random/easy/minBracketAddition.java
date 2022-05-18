import java.util.*;

class Solution {
    public int solve(String s) {
        int ans = 0;
        int balance = 0;
        for (char c : s.toCharArray()) {
            balance += c == '(' ? 1 : -1;
            if (balance == -1) {
                ans++; 
                balance++;
            }
        }
        return balance + ans;
    }
}
