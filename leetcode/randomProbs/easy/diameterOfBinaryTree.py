# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def depth(root, ans):
            if not root: return 0
            paths = []
            for i in children:
                if i:
                    paths[i] = depth(paths, ans)
            ans[0] = max(ans[0], left+right)
            return 1 + max(left, right)
        ans = [0]
        depth(root, ans)
        return ans[0]
