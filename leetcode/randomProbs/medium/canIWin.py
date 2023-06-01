class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        dp = {}
        a,b = maxChoosableInteger, desiredTotal
        t = a*(a+1)/2
        if t < b: return False
        if t == b: return a % 2
        def win(choices, rem):
            if choices[-1] >= rem:
                return True
            k = tuple(choices)
            if k in dp:
                return dp[k]
            for i in range(len(choices)):
                if not win(choices[:i]+choices[i+1:], rem - choices[i]):
                    dp[k] = True
                    return True
            dp[k] = False
            return False
        return win(list(range(1, a+1)), b)
