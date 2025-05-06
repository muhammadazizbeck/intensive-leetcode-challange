class Solution(object):
    def shuffle(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: List[int]
        """
        length = len(nums)
        m = length//2
        list1 = nums[:m]
        list2 = nums[m:]
        listered = []
        for i in range(m):
            listered.append(list1[i])
            listered.append(list2[i])
        return listered