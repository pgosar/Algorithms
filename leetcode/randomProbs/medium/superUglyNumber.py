class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        dp, idx, found = [1], [0]*len(primes), [1]*len(primes)
        s = 1
        for i in range(1, n):
            for j in range(len(primes)):
                if s == found[j]:
                    found[j] = dp[idx[j]] * primes[j]
                    idx[j] += 1
            s = min(found)
            dp.append(s)
        return dp[-1] 
