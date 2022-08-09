class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        count = 1
        for i in range(len(nums)-1):
            if nums[i] != nums[i+1]:
                nums[count] = nums[i+1]
                count+=1
        return count


# 2

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        nums[:] = sorted(set(nums))
        return len(nums)
