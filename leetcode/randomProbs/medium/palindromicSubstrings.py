class Solution:
    def countSubstrings(self, s: str) -> int:
        ans = 0
        n = len(s)
        for i in range(2*n-1):
            left = i // 2
            right = left + i % 2
            while left >= 0 and right < n and s[left] == s[right]:
                left -= 1
                right += 1
                ans += 1
        return ans
