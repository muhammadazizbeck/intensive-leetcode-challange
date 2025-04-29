class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = nums.count(0)
        m = nums.count(1)
        i = 0
        for i in range(len(nums)):
            if i<n:
                nums[i]=0
            elif i>=n and i<n+m:
                nums[i]=1
            else:
                nums[i]=2
        return nums