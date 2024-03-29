class Solution:
    def mySqrt(self, x: int) -> int:
        low = 0
        high = x
        while low <= high:
            mid = (low + high) // 2
            if mid * mid <= x < (mid+1) * (mid+1):
                return mid
            elif mid * mid > x:
                high = mid - 1
            else:
                low = mid + 1
