# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        ans = []
        def helper(root, ans):
            if root.left: helper(root.left, ans)
            if root: ans.append(root.val)
            if root.right: helper(root.right, ans)
            return ans
        if not root: return []
        return helper(root, ans)
