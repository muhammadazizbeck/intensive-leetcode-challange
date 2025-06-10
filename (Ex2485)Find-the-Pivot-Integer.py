class Solution(object):
    def pivotInteger(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n==1:
            return 1
        nums = list(range(1,n+1))
        for i in range(len(nums)-1):
            if sum(nums[:i+1])==sum(nums[i:]):
                return nums[i]
        return -1