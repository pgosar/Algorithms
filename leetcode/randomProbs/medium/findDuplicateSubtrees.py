# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        def dfs(root):
            if not root:
                return "None"
            path = f"{root.val} {dfs(root.left)} {dfs(root.right)}"
            nodes[path].append(root)
            return path
        nodes = defaultdict(list)
        dfs(root)
        return [nodes[path][0] for path in nodes if len(nodes[path]) > 1]
