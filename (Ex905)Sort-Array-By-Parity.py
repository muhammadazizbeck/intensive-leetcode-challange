class Solution(object):
    def sortArrayByParity(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # solution1
        # even_nums = [num for num in nums if num % 2 == 0]
        # odd_nums = [num for num in nums if num % 2 == 1]
        # return even_nums + odd_nums

        # solution2
        final = []
        for num in nums:
            if num % 2 == 0:
                final.insert(0,num)
            else:
                final.append(num)
        return final