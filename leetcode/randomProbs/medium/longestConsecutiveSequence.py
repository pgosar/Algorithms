class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums, ans = set(nums), 0
        for i in nums:
            j = i+1
            if i-1 not in nums:
                while j in nums:
                    j+=1
                ans = max(ans, j-i)
        return ans
