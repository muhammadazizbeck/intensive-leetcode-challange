class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        # solution1
        # while num >= 10:
        #     num = sum([int(digit) for digit in str(num)])
        # return num

        # solution2
        while num >= 10:
            num_str = str(num)
            num = sum(int(digit) for digit in num_str)
        return num