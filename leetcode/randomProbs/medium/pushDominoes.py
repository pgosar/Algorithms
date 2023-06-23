class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        ans = list(dominoes)
        right = float('-inf')
        dp = [0] * len(dominoes)
        for i, c in enumerate(ans):
            if c=='R':
                right = 0
            elif c=='L':
                right = float('-inf')
            elif right != float('-inf'):
                right += 1
                dp[i] = right
                ans[i] = 'R'
        left = float('-inf')
        for i in range(len(ans) -1, -1, -1):
            if dominoes[i] == 'L':
                left = 0
            elif dominoes[i] == 'R':
                left = float('-inf')
            elif left != float('-inf'):
                left += 1
                if left < dp[i] or ans[i] == '.':
                    ans[i] = 'L'
                elif left == dp[i]:
                    ans[i] = '.'
        return ''.join(ans)
