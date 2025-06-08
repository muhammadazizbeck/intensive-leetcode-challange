class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        txt = []
        for i in range(len(nums)):
            counter = 0
            for j in range(len(nums)):
                if nums[j]<nums[i]:
                    counter += 1
            txt.append(counter)
        return txt