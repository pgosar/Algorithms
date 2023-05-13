class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        high, low = 0, float('inf')
        ans = 0
        for i in range(len(prices)):
            low = min(low, prices[i])
            high = max(high, prices[i] - low)
        return high
