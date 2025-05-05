class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # solution1
        settr = list(set(nums))
        settr.sort()
        if len(settr) < 3:
            return max(settr)
        else:
            return settr[-3]