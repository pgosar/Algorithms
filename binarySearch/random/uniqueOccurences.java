import java.util.*;

class Solution {
    public boolean solve(int[] nums) {
        HashMap<Integer, Integer> occurences = new HashMap<>();
        for (int i = 0; i < nums.length; i++) {
            if (!occurences.containsKey(nums[i])) {
                occurences.put(nums[i], 1);
            } else {
                occurences.put(nums[i], occurences.get(nums[i]) + 1);
            }
        }
        HashSet<Integer> numOccurs = new HashSet<>();
        for (Integer num : occurences.values()) {
            numOccurs.add(num);
        }
        return occurences.size() == numOccurs.size();
    }
}
