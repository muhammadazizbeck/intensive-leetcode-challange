class Solution(object):
    def maxProduct(self, n):
        """
        :type n: int
        :rtype: int
        """
        # solution1
        if len(str(n))==1:
            return n
        if len(str(n))==2:
            return int(str(n)[0])*int(str(n)[1])

        digits = [int(num) for num in str(n)]
        digits.sort()
        return digits[-1]*digits[-2]

        # solution2
        # digits = [int(num) for num in str(n)]
        # digits.sort(reverse=True)
        # if len(digits)==1:
        #     return digits[0]
        # else:
        #     return digits[0]*digits[1]