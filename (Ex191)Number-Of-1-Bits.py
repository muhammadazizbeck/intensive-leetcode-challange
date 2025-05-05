class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        # solution1
        # ret = bin(n)[2:]
        # counter = 0
        # for x in ret:
        #     if x == "1":
        #         counter += 1
        # return counter

        # solution2
        # counter = 0
        # while n>0:
        #     if n % 2 == 1:
        #         counter += 1
        #         n = n // 2
        #     else:
        #         n = n // 2
        # return counter
            
        # solution3
        return bin(n)[2:].count("1")