# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        def helper(root, ans):
            if root.left: helper(root.left, ans)
            if root.right: helper(root.right, ans)
            if root: ans.append(root.val)
            return ans
        if not root: return []
        return helper(root, ans)
