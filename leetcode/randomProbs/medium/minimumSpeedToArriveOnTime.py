class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        if len(dist)-1 >= hour:
            return -1
        l, r = 1, 10**7
        ans = 0
        while l <= r:
            m = (l+r)//2
            time = sum(ceil(i/m) for i in dist[:len(dist)-1])
            time += dist[-1]/m
            if time > hour:
                l = m+1
            else:
                r = m-1
                ans = r
        return ans+1
