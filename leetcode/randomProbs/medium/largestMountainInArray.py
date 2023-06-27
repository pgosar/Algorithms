class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        ans = up = down = 0
        if len(arr) < 3: return 0
        for i in range(1, len(arr)):
            if down and arr[i] > arr[i-1] or arr[i] == arr[i-1]:
                up = down = 0
            up += arr[i] > arr[i-1]
            down += arr[i] < arr[i-1]
            if up and down:
                ans = max(ans, up+down+1)
        return ans
