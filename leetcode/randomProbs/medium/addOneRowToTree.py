# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if depth == 1:
            tmp = TreeNode(val)
            tmp.left = root
            return tmp

        def dfs(node, val, depth, cur_depth):
            if not node:
                return
            if cur_depth == depth - 1:
                l = node.left
                r = node.right
                node.left = TreeNode(val)
                node.left.left = l
                node.right = TreeNode(val)
                node.right.right = r
            else:
                dfs(node.left, val, depth, cur_depth + 1)
                dfs(node.right, val, depth, cur_depth + 1)

        dfs(root, val, depth, 1)
        return root
