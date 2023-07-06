# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        ans = 0
        def dfs(root, left):
            if not root:
                return 0
            if left and not root.left and not root.right:
                return root.val
            return dfs(root.left, True) + dfs(root.right, False)
        return dfs(root, False)

        # q = deque([(root, False)])
        # while q:
        #     node, left = q.pop()
        #     if left and not node.left and not node.right:
        #         ans += node.val
        #     if node.left:
        #         q.append((node.left, True))
        #     if node.right:
        #         q.append((node.right, False))
        # return ans
