class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if 0 not in nums:
            return True
        else:
            end = 0
            for i in range(len(nums)):
                if end < i: return False
                end = max(end, i+nums[i])
        return True
