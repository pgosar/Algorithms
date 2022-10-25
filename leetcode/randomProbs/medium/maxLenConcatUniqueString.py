class Solution:
    def maxLength(self, arr: List[str]) -> int:
        mx = 0
        sub = ['']
        for i in arr:
            for j in sub:
                tmp = i + j
                if len(tmp) == len(set(tmp)):
                    sub.append(tmp)
                    mx = max(mx, len(tmp))
        return mx
