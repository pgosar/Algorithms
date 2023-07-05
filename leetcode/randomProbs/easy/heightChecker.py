class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        return sum(1 for i, h in enumerate(sorted(heights)) if h != heights[i])
