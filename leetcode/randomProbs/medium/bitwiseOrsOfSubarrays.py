class Solution:
    def subarrayBitwiseORs(self, arr: List[int]) -> int:
        ans, tmp = set(), set()
        for i in arr:
            ans = {i | j for j in ans}
            ans.add(i)
            tmp |= ans
        return len(tmp)
