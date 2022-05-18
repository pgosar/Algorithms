class Solution:
    def arrayNesting(self, nums):
        
        count = 0

        for i in nums:
            count2 = 0
            
            if i == -1:
                continue
            
            while nums[i] != -1:
                
                count2+=1
                nums[i], i = -1, nums[i]
                
            count = max(count, count2)
        return count