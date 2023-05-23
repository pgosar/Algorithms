class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        ans = [False] * (len(s)+1)
        ans[0] = True
        for i in range(1, len(s)+1):
            for j in range(i):
                if ans[j] and s[j:i] in wordDict:
                    ans[i] = True
                    break
        return ans[-1]
