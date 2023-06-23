class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        if not k or n >= k+maxPts: return 1.0

        dp, x = [1]+[0]*n, 1
        for i in range(1, n+1):
            dp[i] = x / maxPts
            if i < k:
                x += dp[i]
            if i >= maxPts:
                x -= dp[i-maxPts]

        return sum(dp[k:])
