class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # solution1
        # name:set
        # s = set(nums)
        # i = 1
        # while i in s:
        #     i += 1
        # return i

        # solution2
        # name:cyclic sort
        n = len(nums)
        for i in range(n):
            while 1 <= nums[i] <= n and nums[nums[i]-1] != nums[i]:
                nums[nums[i]-1], nums[i] = nums[i], nums[nums[i]-1]
        
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1
        return n + 1