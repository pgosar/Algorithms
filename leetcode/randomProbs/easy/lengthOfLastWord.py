class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        count = 0
        index = len(s) - 1
        while index >= 0 and s[index] == ' ': index-=1
        while index >= 0 and s[index] != ' ':
            count+=1
            index-=1
        return count
