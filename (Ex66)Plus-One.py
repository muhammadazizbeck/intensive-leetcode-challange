class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        # solution1
        # name:simple algorithm
        final_list = []
        total = ''
        for digit in digits:
            total += str(digit)
        final_sum = int(total)+1
        for i in str(final_sum):
            final_list.append(int(i))
        return final_list