class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans, b, s, d, n = 0, 0, 0, 0, len(prices)-1
        while (d < n):
            while d < n and prices[d+1] <= prices[d]:
                d+=1
            b = prices[d]
            while d < n and prices[d+1] > prices[d]:
                d+=1
            s = prices[d]
            ans += s-b
        return ans
