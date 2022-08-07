class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]
        def helper(newNums):
            rob1, rob2 = 0, 0
            for n in newNums:
                temp = max(rob1 + n, rob2)
                rob1 = rob2
                rob2 = temp
            return max(rob1, rob2)
        return max(helper(nums[1:]), helper(nums[:-1]))
