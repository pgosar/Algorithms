class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def helper(nums, tmp, ans):
            if not nums:
                ans.append(tmp)
                return
            for i in range(len(nums)):
                helper(nums[:i] + nums[i+1:], tmp+[nums[i]], ans)
        ans = []
        helper(nums, [], ans)
        return ans
