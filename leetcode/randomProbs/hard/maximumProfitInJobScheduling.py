class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        jobs = sorted(zip(startTime, endTime, profit), key=lambda x: x[0])
        heap = []
        cur = mx = ans = 0
        for s, e, p in jobs:
            while heap and heap[0][0] <= s:
                _, tmp = heapq.heappop(heap)
                cur = max(cur,tmp)
            heapq.heappush(heap, (e,p+cur))
            ans = max(ans, cur+p)
        return ans
