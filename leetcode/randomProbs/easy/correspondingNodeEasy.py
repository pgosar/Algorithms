# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        def helper(cloned, target):
            if(not cloned or cloned.val==target.val):
                return cloned
            return helper(cloned.left,target) or helper(cloned.right,target)

        return helper(cloned,target)
