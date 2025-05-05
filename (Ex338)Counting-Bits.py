class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        res = []
        start = 0
        while start <= n:
            counter = bin(n)[2:].count("1")
            res.append(counter)
            start += 1
        return res