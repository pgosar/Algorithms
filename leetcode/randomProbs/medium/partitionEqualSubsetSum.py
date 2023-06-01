class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        ans, t, n = 0, sum(nums), len(nums)
        if t & 1 == 1:
            return False
        t //= 2
        dp = [False] * (t+1)
        dp[0] = True
        for i in nums:
            for j in range(t, 0, -1):
                if j >= i:
                    dp[j] = dp[j] or dp[j-i]
        print(dp)
        return dp[-1]
