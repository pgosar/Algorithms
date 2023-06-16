class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        sell, keep = 0, float('-inf')
        for i in prices:
            sell = max(sell, i-fee+keep)
            keep = max(keep, sell-i)
        return sell
