# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        def helper(root, e):
            if root > e:
                return [None]
            trees = []
            for i in range(root, e+1):
                left = helper(root, i-1)
                right = helper(i+1, e)
                for l in left:
                    for r in right:
                        roo = TreeNode(i, l, r)
                        trees.append(roo)
            return trees
        return helper(1, n)

