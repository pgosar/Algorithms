class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        def less(x):
            count = 0
            c = n-1
            for i in range(m):
                while c >= 0 and x < matrix[i][c]:
                    c-=1
                count += (c+1)
            return count

        m, n = len(matrix), len(matrix[0])
        l, r = matrix[0][0], matrix[-1][-1]
        ans = -1
        while l <= r:
            mid = (l+r)//2
            if less(mid) >= k:
                ans = mid
                r = mid-1
            else:
                l = mid+1
        return ans
