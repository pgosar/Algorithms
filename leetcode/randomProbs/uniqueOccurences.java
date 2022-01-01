class Solution {
    public boolean uniqueOccurrences(int[] arr) {
        HashMap<Integer, Integer> occurences = new HashMap<>();
        for (int i = 0; i < arr.length; i++) {
            if (!occurences.containsKey(arr[i])) {
                occurences.put(arr[i], 1);
            } else {
                occurences.put(arr[i], occurences.get(arr[i]) + 1);
            }
        }
        HashSet<Integer> numOccurs = new HashSet<>();
        for (Integer num : occurences.values()) {
            numOccurs.add(num);
        }
        return occurences.size() == numOccurs.size();
    }
}
