class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        settr = set(nums)
        return (3*sum(settr) - sum(nums)) // 2
        