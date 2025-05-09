class Solution(object):
    def sortArrayByParityII(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []
        odd = [num for num in nums if num % 2 == 1]
        even = [num for num in nums if num % 2 == 0]
        for i in range(len(even)):
            res.append(even[i])
            res.append(odd[i])
        return res