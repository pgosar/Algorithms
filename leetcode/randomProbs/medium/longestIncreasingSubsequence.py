class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        tails = [0] * len(nums)
        size = 0
        for num in nums:
            l, r = 0, size
            while l != r:
                m = l + (r - l) // 2
                if tails[m] < num:
                    l = m + 1
                else:
                    r = m
            tails[l] = num
            size = max(size, l + 1)
        return size
