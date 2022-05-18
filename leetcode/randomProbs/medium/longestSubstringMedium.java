class Solution {
    public int lengthOfLongestSubstring(String s) {
        int[] characters = new int[256];
        int left = 0
        int right = 0;
        int count = 0;
        while (right < s.length()) {
            characters[s.charAt(right)]++;
            while (characters[s.charAt(right)] > 1) {
                characters[s.charAt(left)]--;
                left++;
            }
            count = Math.max(count, right - left + 1);
            right++;
        }
        return count;
    }
}

