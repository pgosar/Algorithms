class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals = sorted(intervals, key=lambda x: x[1])
        end = float('-inf')
        ans = 0
        for a, b in intervals:
            if a >= end:
                end = b
            else:
                ans += 1
        return ans
