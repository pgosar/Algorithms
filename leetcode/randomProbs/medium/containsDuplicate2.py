class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        d = {}
        for i, c in enumerate(nums):
            if c in d and abs(d[c] - i) <= k:
                return True
            d[c] = i
        return False
