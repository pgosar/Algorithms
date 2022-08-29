class Solution:
    def solve(self, s):
        ans = []
        left = right = 0
        lastIndex = {c: i for i, c in enumerate(s)}

        for i, c in enumerate(s):
            right = max(right, lastIndex[c])
            if i == right:
                ans.append(right - left + 1)
                left = right = i + 1

        return ans
