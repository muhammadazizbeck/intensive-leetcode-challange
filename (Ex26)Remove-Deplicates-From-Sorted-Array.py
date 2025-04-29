class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 1
        for j in range(1,len(nums)):
            if nums[j] != nums[j-1]:
                nums[i]=nums[j]
                i += 1
        return i