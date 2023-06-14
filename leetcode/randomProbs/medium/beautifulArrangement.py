class Solution:
    def countArrangement(self, n: int) -> int:
        nums = [i for i in range(1, n+1)]
        ans = 0
        def dfs(nums, i):
            if i == 1:
                return 1

            ans = 0
            for j, c in enumerate(nums):
                if not (c % i and i % c):
                    ans += dfs(nums[:j]+nums[j+1:], i-1)
            return ans
        return dfs(nums, n)
