class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        
        i = 1  
        count = 1 
        
        for j in range(1, len(nums)): 
            if nums[j] == nums[j-1]:
                count += 1  
            else:
                count = 1  
                
            if count <= 2: 
                nums[i] = nums[j]  
                i += 1  
        
        return i