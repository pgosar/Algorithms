class Solution:
    def soupServings(self, n: int) -> float:
        memo = defaultdict()
        def dfs(a, b):
            if (a, b) in memo:
                return memo[(a, b)]
            if n in memo:
                return memo[n]
            if a <= 0 and b > 0:
                memo[(a, b)] = 1
                return 1
            elif a <= 0 and b <= 0:
                memo[(a, b)] = 0.5
                return 0.5
            elif a > 0 and b <= 0:
                memo[(a, b)] = 0
                return 0
            memo[(a, b)] = (dfs(a-4, b) + dfs(a-3, b-1) + dfs(a-2, b-2) + dfs(a-1, b-3)) * 0.25
            return memo[(a, b)]
        if n > 4275:
            memo[n] = 1
            return 1
        n /= 25
        return dfs(n, n)
