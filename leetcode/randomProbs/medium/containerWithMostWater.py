class Solution:
    def maxArea(self, height: List[int]) -> int:
        area = 0
        i, j = 0, len(height) - 1
        while i <=j:
            area = max(area, (j-i) * min(height[i], height[j]))
            if height[i] > height[j]:
                j-=1
            else:
                i+=1
        return area
