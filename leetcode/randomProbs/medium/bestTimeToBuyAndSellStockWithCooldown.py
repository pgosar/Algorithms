class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = float('inf')
        free,last,now = 0,0,0
        for i in prices:
            now = max(last,i-buy )
            buy = min(buy,i-free )
            free,last = last,now
        return now
