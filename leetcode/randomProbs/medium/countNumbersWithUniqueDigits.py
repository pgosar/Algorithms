class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        if n == 0:
            return 1
        ans, start = 10, 9
        for i in range(1, n):
            start *= (10-i)
            ans += start
        return ans
