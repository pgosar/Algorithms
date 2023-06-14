class Solution:
    def optimalDivision(self, nums: List[int]) -> str:
        return '/'.join(map(str, nums)) if len(nums) <= 2 else f"{str(nums[0])}/({'/'.join(map(str, nums[1:]))})"
