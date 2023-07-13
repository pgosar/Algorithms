class Solution:
    def isUgly(self, n: int) -> bool:
        return n > 0 == (2*3*5)**22 % n == 0
