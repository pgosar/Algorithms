class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        one = two = 0
        for i in nums:
            one = (one ^ i) & ~two
            two = (two ^ i) & ~one
        return one
