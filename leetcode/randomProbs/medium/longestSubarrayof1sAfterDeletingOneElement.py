
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        mx = ans = prev = 0
        for i in nums:
            if i == 1:
                mx += 1
                ans = max(ans, mx+prev)
            else:
                prev, mx = mx, 0
        return ans - (ans == len(nums))
