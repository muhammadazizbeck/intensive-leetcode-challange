class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        # solution = 1
        # left,right = 0,len(s)-1
        # while left<right:
        #     s[left],s[right]=s[right],s[left]
        #     left += 1
        #     right -= 1

        # solution2
        s[:] = s[::-1]