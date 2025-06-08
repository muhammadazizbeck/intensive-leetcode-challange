class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []
        counter = 0
        for num in nums:
            counter += num
            res.append(counter)
        return res