class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        ans, end = 0, float('-inf')
        for s, t in sorted(pairs, key =lambda x: x[1]):
            end, ans = (t, ans+1) if s > end else (end, ans)
        return ans
