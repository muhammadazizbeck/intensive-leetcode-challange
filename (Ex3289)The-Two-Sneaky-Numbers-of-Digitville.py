class Solution(object):
    def getSneakyNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        arr = []
        counter = Counter(nums)
        for value,times in counter.items():
            if times==2:
                arr.append(value)
        return arr 