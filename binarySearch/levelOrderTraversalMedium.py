class Solution:
    def solve(self, root):
        answer = []
        level = [root]
        while root and level:
            curr = []
            nextLevel = []
            for node in level:
                curr.append(node.val)
                if node.left:
                    nextLevel.append(node.left)
                if node.right:
                    nextLevel.append(node.right)
            answer += curr
            level = nextLevel;
        return answer
