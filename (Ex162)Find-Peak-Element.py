class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # solution1
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[mid + 1]:
                right = mid
            else:
                left = mid + 1
        return left

        # solution2
        # def findpeak(left,right):
        #     if left == right:
        #         return left
        #     mid = (left+right)//2
        #     if nums[mid]>nums[mid+1]:
        #         return findpeak(left,mid)
        #     else:
        #         return findpeak(mid+1,right)
        # return findpeak(0,len(nums)-1)