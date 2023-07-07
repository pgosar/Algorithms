class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        return -1 if len(nums) < 3 else sum(nums[0:3]) - min(nums[0:3]) - max(nums[0:3])
