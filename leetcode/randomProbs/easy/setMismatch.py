class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        return [sum(nums) - sum(set(nums)), sum(nums) - sum(set(nums)) + (sum([i + 1 for i in range(len(nums))]) - sum(nums))]
