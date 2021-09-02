class Solution:
    
    def fourSum(self, nums, target):
        
        answer = set()
        nums.sort()
        for i in range(len(nums)):
            
            for j in range(i+1, len(nums)):
                
                start = j+1
                end = len(nums)-1
                remaining = target - nums[j] - nums[i]
                
                while start < end:
                    
                    if remaining == nums[start]+nums[end]:
                        answer.add((nums[start], nums[end], nums[i], nums[j]))
                        
                        start+=1
                        end-=1
                    
                    elif remaining < nums[start]+nums[end]:

                        end -=1
                    else:
                        start +=1
        return answer
                
                
                