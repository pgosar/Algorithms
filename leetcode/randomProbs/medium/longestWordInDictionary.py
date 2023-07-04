class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        dictionary.sort(key=lambda x: (-len(x), x))
        ans = 0
        for i in dictionary:
            idx = 0
            for c in s:
                if idx < len(i) and c == i[idx]:
                    idx += 1
            if idx == len(i):
                return i
        return ""
