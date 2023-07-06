class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        j, s, ans = 0, 0, len(nums)+1
        for i in range(len(nums)):
            s+= nums[i]
            while s >= target:
                ans = min(ans, i-j+1)
                s-=nums[j]
                j+=1
        return ans if ans != len(nums)+1 else 0
