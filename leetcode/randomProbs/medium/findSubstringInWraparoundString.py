class Solution:
    def findSubstringInWraproundString(self, s: str) -> int:
        ans = {i:1 for i in s}
        b = 0
        for i in range(len(s)):
            b = b + 1 if (ord(s[i-1])-96) % 26 == (ord(s[i])-97) else 1
            ans[s[i]] = max(ans[s[i]], b)
        return sum(ans.values())
