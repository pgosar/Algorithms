class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        ans = tmp = sum(i*j for i, j in enumerate(nums))
        s = sum(nums)
        l = len(nums)
        while nums:
            tmp += s - (nums.pop() * l)
            ans = max(ans, tmp)
        return ans
