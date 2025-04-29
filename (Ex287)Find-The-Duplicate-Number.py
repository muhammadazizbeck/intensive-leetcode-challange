class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums_counter = Counter(nums)
        for key,val in nums_counter.items():
            if val >= 2:
                return key

        
        