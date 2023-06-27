class Solution:
    def balancedString(self, s: str) -> int:
        cnt = {}
        n = len(s) // 4
        for i in s:
            if i in cnt:
                cnt[i] += 1
            else:
                cnt[i] = 1
        extra = {}
        for i in cnt:
            if cnt[i] > n:
                extra[i] = cnt[i] - n
        if not extra: return 0
        j = 0
        ans = float('inf')
        for i in range(len(s)):
            if s[i] in extra:
                extra[s[i]] -= 1
            while max(extra.values()) <= 0:
                ans = min(i-j+1, ans)
                if s[j] in extra:
                    extra[s[j]] += 1
                j += 1
        return ans
