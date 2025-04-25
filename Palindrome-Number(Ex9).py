class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        # solution1
        # name:checking palindrome
        # return str(x)==str(x)[::-1]

        # solution2
        # name:two pointers
        # final_str = str(x)
        # left,right = 0,len(final_str)-1
        # while left<right:
        #     if final_str[left] != final_str[right]:
        #         return False
        #     else:
        #         left += 1
        #         right -= 1
        # return True

        # solution3
        # name:recursion
        s = str(x)
        def check(left,right):
            if left >= right :
                return True
            if s[left] != s[right]:
                return False
            return check(left+1,right-1)
        return check(0,len(s)-1)