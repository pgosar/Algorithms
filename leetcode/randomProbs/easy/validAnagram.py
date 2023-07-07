class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return defaultdict(int, {char: s.count(char) for char in set(s)}) == defaultdict(int, {char: t.count(char) for char in set(t)})
