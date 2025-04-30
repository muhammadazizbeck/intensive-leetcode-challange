class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = []
        i = 1
        while i <= n:
            if i % 3 == 0 and i % 5 != 0:
                res.append("Fizz")
            elif i % 3 != 0 and i % 5 == 0:
                res.append('Buzz')
            elif i % 3 == 0 and i % 5 == 0:
                res.append("FizzBuzz")
            else:
                res.append(str(i))
            i += 1
        return res