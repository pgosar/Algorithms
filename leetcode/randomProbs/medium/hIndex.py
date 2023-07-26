class Solution:
    def hIndex(self, citations: List[int]) -> int:
        a = sorted(citations, reverse=True)
        ans = 0
        for i in a:
            if i > ans:
                ans += 1
        return ans

        return sum(i < j for i, j in enumerate(sorted(citations, reverse=True)))
