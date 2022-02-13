class Solution {
    public List<List<Integer>> subsets(int[] nums) {
        List<List<Integer>> permutations = new ArrayList<>();
        Arrays.sort(nums);
        helper(permutations, new ArrayList<>(), nums, 0);
        return permutations;
    }

    private void helper(List<List<Integer>> permutations , List<Integer> onePerm, int [] nums, int start){
        permutations.add(new ArrayList<>(onePerm));
        for(int i = start; i < nums.length; i++){
            onePerm.add(nums[i]);
            helper(permutations, onePerm, nums, i + 1);
            onePerm.remove(onePerm.size() - 1);
        }
    }
}
