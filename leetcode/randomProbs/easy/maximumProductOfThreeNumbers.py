class Solution:
    def maximumProduct(self, n: List[int]) -> int:
        return n.sort() and None or max(n[-1]*n[-2]*n[-3], n[0]*n[1]*n[-1])
