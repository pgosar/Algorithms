class Solution:
    def solve(self, a, b):
        ans = [[0 for _ in range(len(a) + 1)] for _ in range(len(b) + 1)]

        for i in range(1, len(a) + 1):
            for j in range(1, len(b) + 1):
                if a[i - 1] == b[i - 1]:
                    ans[i][j] = ans[i - 1][j - 1] + 1
                else:
                    ans[i][j] = max(ans[i][j - 1], ans[i - 1][j])

        return len(a) + len(b) - ans[len(a)][len(b)]
