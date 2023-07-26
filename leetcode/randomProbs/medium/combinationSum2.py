class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
       def dfs(nums, tgt, cur, ans):
            if tgt < 0:
                return
            if tgt == 0:
                ans.append(cur)
                return
            for i in range(len(nums)):
                if nums[i] > target:
                    break
                if i != 0 and nums[i] == nums[i-1]:
                    continue
                dfs(nums[i+1:], tgt-nums[i], cur+[nums[i]], ans)
        ans = []
        dfs(sorted(candidates), target, [], ans)
        return ans return ans
