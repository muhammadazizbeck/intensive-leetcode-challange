class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        linear_count = len(nums)
        total_list = list(range(1,linear_count+1))
        set_nums = set(nums)
        abondened_numbers = []
        for part in total_list:
            if part not in set_nums:
                abondened_numbers.append(part)
        return abondened_numbers
