class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        odd, even, ans, mod = 0, 1, 0, 10**9+7
        cur = 0
        for i in arr:
            cur += i
            if cur % 2 == 1:
                odd += 1
                ans += even
            else:
                even += 1
                ans += odd

        return ans % mod
