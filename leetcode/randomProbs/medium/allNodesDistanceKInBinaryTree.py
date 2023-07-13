# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        def parents(node, parent):
            if not node: return
            d[node] = parent
            parents(node.left, node)
            parents(node.right, node)

        def helper(node, cnt):
            if not node or cnt > k or node in seen:
                return
            seen.add(node)
            if cnt == k:
                nodes.append(node.val)
            helper(node.left, cnt+1)
            helper(node.right, cnt+1)
            helper(d[node], cnt+1)
        nodes = []
        d = {}
        seen = set()
        parents(root, None)
        helper(target, 0)
        return nodes
