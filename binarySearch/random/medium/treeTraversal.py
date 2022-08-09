# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solve(self, root, moves):
        stack = []
        node = root
        for string in moves:
            if string == "LEFT":
                stack.append(node)
                node = node.left
            elif string == "RIGHT":
                stack.append(node)
                node = node.right
            elif string == "UP":
                node = stack.pop()
        return node.val
