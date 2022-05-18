import java.util.*;

class Solution {
    public int solve(int[] nums) {
        int[] right = new int[nums.length];
        int[] left = new int[nums.length];
        int max = 0;
        int count = 0;
        for (int i = nums.length - 1; i >= 0; i--) {
            max = max > nums[i] ? max : nums[i];
            right[i] = max;
        }
        max = 0;
        for (int i = 0; i < nums.length; i++) {
            max = max > nums[i] ? max : nums[i];
            left[i] = max;
            count += (Math.min(left[i], right[i]) - nums[i]);
        }
        return count;
    }
}
