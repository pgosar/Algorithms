class Solution:
    def longestCommonPrefix(self, strs):
        
        string = ""        
        if len(strs)==0:
            return string
        elif len(strs)==1:
            return strs[0]
        
        for i in range(len(min(strs))):
            for j in range(1, len(strs)):
                if(strs[0][i] ==strs[j][i]):
                    if j == len(strs) -1:
                        string += strs[0][i]
                else: return string
        return string