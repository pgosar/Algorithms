class Solution:
    def minPatches(self, nums, n):
        
        missing = 1
        answer = index = 0
        
        while missing <= n:
            
            if index < len(nums) and nums[index] <= missing:
                missing += nums[index]
                index +=1
            
            else:
                answer += 1
                missing += missing
        
        return answer