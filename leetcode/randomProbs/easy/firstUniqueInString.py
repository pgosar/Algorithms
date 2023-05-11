class Solution:
    def firstUniqChar(self, s: str) -> int:
        d = {}
        seen = set()
        for i, c in enumerate(s):
            if c not in seen:
                seen.add(c)
                d[c] = i
            elif c in d:
                del d[c]
        return min(d.values()) if len(d.values()) > 0 else -1
