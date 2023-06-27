class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        ans = []
        heap = []
        vis = set()
        heapq.heappush(heap, (nums1[0]+nums2[0], 0, 0))
        vis.add((0, 0))
        while len(ans) < k and heap:
            _, a, b = heappop(heap)
            ans.append([nums1[a], nums2[b]])
            if a+1 < len(nums1) and (a+1, b) not in vis:
                vis.add((a+1, b))
                heapq.heappush(heap, (nums1[a+1] + nums2[b], a+1, b))
            if b+1 < len(nums2) and (a, b+1) not in vis:
                vis.add((a, b+1))
                heapq.heappush(heap, (nums1[a] + nums2[b+1], a, b+1))
        return ans
