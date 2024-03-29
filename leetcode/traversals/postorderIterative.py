# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        stack = []
        node = root
        while stack or node:
            if node:
                stack.append(node)
                ans.insert(0, node.val)
                node = node.right
            else:
                node = stack.pop()
                node = node.left
        return ans
