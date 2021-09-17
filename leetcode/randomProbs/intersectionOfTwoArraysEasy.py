class Solution():
    def intersect(self, nums1, nums2):

        def binarySearch(nums, target):
            left = 0
            right = len(nums) - 1
            while left <= right:
                mid = (left + right) // 2
                if(nums[mid] == target):
                    nums.pop(mid)
                    return True
                elif nums[mid] > target:
                    right = mid - 1
                elif nums[mid] < target:
                    left = mid + 1
            return False

        nums1.sort()
        nums2.sort()
        answer = []

        for i in nums1:
            if binarySearch(nums2, i):
                answer.append(i)

        return answer

