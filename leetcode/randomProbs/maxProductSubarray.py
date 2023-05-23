class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        p, s, m = 0, 0, float('-inf')
        for i in range(len(nums)):
            p = (p or 1) * nums[i]
            s = (s or 1) * nums[::-1][i]
            m = max(m, p, s)
        return m
