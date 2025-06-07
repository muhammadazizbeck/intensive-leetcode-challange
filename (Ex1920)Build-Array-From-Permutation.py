class Solution(object):
    def buildArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # solution1
        # arr = []
        # for i in range(len(nums)):
        #     arr.append(nums[nums[i]])
        # return arr

        # solution2
        arr = []
        for num in nums:
            arr.append(nums[num])

        return arr