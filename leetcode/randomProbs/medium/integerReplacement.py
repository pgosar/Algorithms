class Solution:
    def integerReplacement(self, n: int) -> int:
        ans = 0
        while n != 1:
            if n % 4 == 1 or n == 3:
                n -= 1
            elif n % 4 == 3:
                n += 1
            else:
                n = n // 2
            ans += 1
        return ans
