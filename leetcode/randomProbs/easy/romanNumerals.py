class Solution:
    def romanToInt(self, s: str) -> int:
        ans, prev = 0, 0
        conv = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        for sym in s[::-1]:
            if (conv[sym] >= prev):
                ans+=conv[sym]
            else:
                ans-=conv[sym]
            prev = conv[sym]
        return ans
