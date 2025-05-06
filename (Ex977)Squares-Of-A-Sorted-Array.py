class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # solution1
        final_list = sorted([digit**2 for digit in nums])
        return final_list
