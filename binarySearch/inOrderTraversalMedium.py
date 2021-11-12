class Solution:
    def solve(self, root):
        answer, stack = [], []
        while True:
            while root:
                stack.append(root)
                root = root.left
            if not stack:
                return answer
            node = stack.pop()
            answer.append(node.val)
            root = node.right
