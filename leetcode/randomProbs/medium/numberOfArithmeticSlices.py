class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        ans = 0
        prev = 0
        for i in range(2, len(nums)):
            if nums[i-2] - nums[i-1] == nums[i-1] - nums[i]:
                prev += 1
                ans += prev
            else:
                prev = 0
        return ans
