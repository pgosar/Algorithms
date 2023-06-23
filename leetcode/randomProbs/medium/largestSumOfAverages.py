class Solution:
    def largestSumOfAverages(self, nums: List[int], k: int) -> float:
        n = len(nums)
        dp = [0]
        for i in nums:
            dp.append(dp[-1] + i)
        def solve(i, k):
            if(k == 1): return sum(nums[i:])/(n-i)
            if(n-i < k): return -1
            if((i, k) in d): return d[(i, k)]
            tmp = 0
            for j in range(i+1, n):
                tmp = max(tmp, solve(j, k-1)+(dp[j]-dp[i])/(j-i))
            d[(i, k)] = tmp
            return tmp
        d = dict()
        return solve(0, k)
