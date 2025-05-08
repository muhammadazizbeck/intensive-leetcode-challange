class Solution(object):
    def countPairs(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # solution1
        # counter = 0
        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)):
        #         if nums[i]+nums[j]<target:
        #             counter += 1

        # return counter
        nums.sort()
        counter = 0
        left,right = 0,len(nums)-1
        while left<right:
            if nums[left]+nums[right]<target:
                counter += (right-left)
                left += 1
            else:
                right -= 1
        return counter