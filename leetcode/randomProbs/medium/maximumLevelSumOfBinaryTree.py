# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        q = deque([root])
        mx, level, ans = -float('inf'), 0, 0
        while q:
            level += 1
            s = 0
            for _ in range(len(q)):
                node = q.popleft()
                s += node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            if mx < s:
                mx, ans = s, level
        return ans

        def dfs(root, ans, level):
            if not root:
                return
            if level == len(ans):
                ans.append(root.val)
            else:
                ans[level] += root.val
            dfs(root.left, ans, level+1)
            dfs(root.right, ans, level+1)
        ans = []
        dfs(root, ans, 0)
        return 1+ans.index(max(ans))
