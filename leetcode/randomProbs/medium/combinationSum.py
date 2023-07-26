class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(nums, tgt, cur, ans):
            if tgt < 0:
                return
            if tgt == 0:
                ans.append(cur)
            for i in range(len(nums)):
                dfs(nums[i:], tgt-nums[i], cur+[nums[i]], ans)
        ans = []
        dfs(candidates, target, [], ans)
        return ans
