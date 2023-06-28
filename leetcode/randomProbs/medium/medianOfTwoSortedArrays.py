class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        a = b = 0
        n, m = len(nums1), len(nums2)
        a1, a2 = 0, 0
        mid = (n + m) // 2 + 1
        for _ in range(mid):
            a2 = a1
            if b == m or (a != n and nums1[a] <= nums2[b]):
                a1 = nums1[a]
                a += 1
            else:
                a1 = nums2[b]
                b += 1
        return a1 if (m+n) & 1 != 0 else (a1 + a2) / 2


# log(m+n) sol

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        def helper(a, b, s1, e1, s2, e2, m):
            if s1 > e1:
                return b[m-s1]
            if s2 > e2:
                return a[m-s2]
            m1, m2 = (s1+e1) // 2, (s2+e2) // 2
            v1, v2 = a[m1], b[m2]
            if m1+m2 < m:
                if v1 > v2:
                    return helper(a, b, s1, e1, m2+1, e2, m)
                else:
                    return helper(a, b, m1+1, e1, s2, e2, m)
            else:
                if v1 > v2:
                    return helper(a, b, s1, m1-1, s2, e2, m)
                else:
                    return helper(a, b, s1, e1, s2, m2-1, m)


        n, m = len(nums1), len(nums2)
        mid = (n+m) // 2
        if (n+m) % 2 == 1:
            return helper(nums1, nums2, 0, n-1, 0, m-1, mid)
        else:
            return (helper(nums1, nums2, 0, n-1, 0, m-1, mid) + helper(nums1, nums2, 0, n-1, 0, m-1, mid-1)) / 2
