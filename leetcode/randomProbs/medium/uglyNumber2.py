class Solution:
    def nthUglyNumber(self, n: int) -> int:
        ans, a, b, c = [0]*n, 0, 0, 0
        ans[0] =1
        for i in range(1, n):
            ans[i] = min(ans[a]*2, ans[b]*3, ans[c]*5)
            if ans[i] == ans[a]*2: a+=1
            if ans[i] == ans[b]*3: b+=1
            if ans[i] == ans[c]*5: c+=1
        return ans[-1]
