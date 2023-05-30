class Solution:
    def integerBreak(self, n: int) -> int:
        rem = [1, 4, 2]
        if n < 4:
            return n-1
        elif n % 3 != 1:
            return 3**(n//3) * rem[n%3]
        else:
            return 3**(n//3-1) * rem[n%3]
