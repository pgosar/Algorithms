class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return (x := reduce(lambda x, y: x ^ y, nums))
