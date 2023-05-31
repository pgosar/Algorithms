class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums = sorted(nums)
        dp = [[i] for i in nums]
        for i in range(len(nums)):
            for j in range(i):
                if nums[i] % nums[j] == 0 and len(dp[j]) >= len(dp[i]):
                    dp[i] = dp[j] + [nums[i]]
        print(dp)
        return max(dp, key=len)
