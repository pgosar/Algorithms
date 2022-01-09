class Solution {
    public int trap(int[] height) {
        int count = 0;
        int[] left = new int[height.length];
        int[] right = new int[height.length];
        int max = 0;
        
        for (int i = height.length - 1; i >= 0; i--) {
            max = max > height[i] ? max : height[i];
            right[i] = max;
        }
        max = 0;
        for (int i = 0; i < height.length; i++) {
            max = max > height[i] ? max : height[i];
            left[i] = max;
            int minValue = Math.min(left[i], right[i]);
            count += (minValue - height[i]);
        }
        return count;
    }
}
