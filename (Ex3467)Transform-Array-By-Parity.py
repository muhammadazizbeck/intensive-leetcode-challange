class Solution(object):
    def transformArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # solution1
        # even = [0 for digit in nums if digit % 2 == 0]
        # odd = [1 for digit in nums if digit % 2 == 1]
        # return even+odd

        # solution2
        lister = []
        for num in nums:
            if num % 2 == 0:
                lister.append(0)
            else:
                lister.append(1)
        return sorted(lister)