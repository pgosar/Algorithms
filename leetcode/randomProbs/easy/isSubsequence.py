class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        idx = 0
        for i in s:
            print(t[idx:])
            if i in t[idx:]:
                idx += t[idx:].index(i) + 1
            else:
                return False
        return True
