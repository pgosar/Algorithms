import java.util.*;

class Solution {
    public int solve(int[] nums) {
        if (nums.length == 0) return 0;
        if (nums.length == 1) return 1;
        int[] ans = new int[nums.length];
        int answer = 0;
        for (int i = 1; i < nums.length; i++) {
            for (int j = 0; j < i; j++) {
                if (nums[j] < nums[i]) {
                    ans[i] = Math.max(ans[i], ans[j] + 1);
                }
            }
            answer = Math.max(answer, ans[i]);
        }
        return answer + 1;
    }
}
