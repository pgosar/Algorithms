import java.util.*;

class Solution {
    public boolean solve(String s) {
        int[] characters = new int[256];
        for (char c : s.toCharArray()) {
            if (characters[c] == 0) {
                characters[c]++;
            } else {
                characters[c]--;
            }
        }
        int count = 0;
        for (int i = 0; i < characters.length; i++) {
            if (characters[i] > 0) count++;
        }
        return count <= 1;
    }
}
