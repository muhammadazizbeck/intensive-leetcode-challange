class Solution(object):
    def rearrangeArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        arr = []
        negative_nums = [num for num in nums if num<0]
        positive_nums = [num for num in nums if num>0]
        for i in range(len(positive_nums)):
            arr.append(positive_nums[i])
            arr.append(negative_nums[i])
        return arr