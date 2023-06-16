class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        pts, prev, cur = [0]*(max(nums)+1), 0, 0
        for i in nums:
            pts[i] += i
        for i in pts:
            prev, cur = cur, max(prev+i, cur)
        return cur
