class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        nums = set(arr)
        ans, mx = 0, 2
        for i in range(len(arr)):
            for j in range(i+1, len(arr)):
                a, b = arr[i], arr[j]
                mx = 2
                while a + b in nums:
                    a, b = b, a+b
                    mx +=1
                if mx > 2:
                    ans = max(ans, mx)
        return ans
