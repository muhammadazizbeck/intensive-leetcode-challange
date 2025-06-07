class Solution(object):
    def pivotArray(self, nums, pivot):
        """
        :type nums: List[int]
        :type pivot: int
        :rtype: List[int]
        """
        arr1 = [num for num in nums if num < pivot]
        arr2 = [num for num in nums if num == pivot]
        arr3 = [num for num in nums if num > pivot]
        return arr1+arr2+arr3