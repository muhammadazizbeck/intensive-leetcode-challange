# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        # solution1
        # left,right=0,n
        # while left<=right:
        #     mid = (left+right)//2
        #     res = guess(mid)
        #     if res == 0:
        #         return mid
        #     if res == 1:
        #         left = mid + 1
        #     if res == -1:
        #         right = mid -1 
        # return -1
        guess = None
        # solution2
        def search(left, right):
            mid = (left + right) // 2
            res = guess(mid)
            if res == 0:
                return mid
            elif res == 1:
                return search(mid + 1, right)
            else:
                return search(left, mid - 1)
        return search(1, n)