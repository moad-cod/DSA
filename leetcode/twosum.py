class Solution(object):
    def twoSum(self, nums, target):
        if len(nums) < 2:
            return []
        
        
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:    
                    return [i, j]
        
        return []
    
    # # Hash Map
    def twoSum_HM(self, nums, target):
        if len(nums) < 2:
            return []
        
        seen = {}
        
        for i, num in enumerate(nums):
            
            complement = target - num
            
            if complement in seen:
                return [seen[complement], i]
        
            seen[num] = i
            
        return []

nums = [2,7,11,15, 4, 5]
target = 9

print(Solution().twoSum(nums, target))
print(Solution().twoSum_HM(nums, target))

