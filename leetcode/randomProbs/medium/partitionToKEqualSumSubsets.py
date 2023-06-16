class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        req = sum(nums) // k
        dp = [0]*k
        nums.sort(reverse=True)

        def dfs(i):
            if i == len(nums):
                return True

            for j in range(k):
                if dp[j] + nums[i] <= req:
                    dp[j] += nums[i]
                    if(dfs(i+1)):
                        return True
                    dp[j] -= nums[i]
                if dp[j] == 0: break
            return False
        return dfs(0)
