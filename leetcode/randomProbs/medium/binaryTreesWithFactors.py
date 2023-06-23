class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        arr.sort()
        MOD = 10**9+7
        dp = {n: 1 for n in arr}
        for i, c in enumerate(arr):
            for j in range(i):
                if not c % arr[j] and c // arr[j] in dp:
                    dp[c] += dp[arr[j]] * dp[c//arr[j]]
                    dp[c] %= MOD
        return sum(dp.values()) % MOD
