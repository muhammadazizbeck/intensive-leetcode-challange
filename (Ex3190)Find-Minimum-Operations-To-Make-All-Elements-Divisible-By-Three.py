class Solution(object):
    def minimumOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # solution1
        # counter = 0
        # for num in nums:
        #     if num % 3 != 0:
        #         counter += 1
        # return counter

        # solution2
        next_list = [num for num in nums if num % 3 != 0]
        return len(next_list)