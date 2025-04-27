class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        # solution1
        # name = brute force
        # n = len(s)
        # if n < 2:
        #     return s
        # longest = ''
        # for i in range(n):
        #     for j in range(i+1,n+1):
        #         substr = s[i:j]
        #         if substr == substr[::-1] and len(substr)>len(longest):
        #             longest = substr
        # return longest

        # solution2
        # name:two pointers
        if len(s) < 1:
            return s
    
        def expand_from_center(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1:right]

        longest = ""
        
        for i in range(len(s)):
            palindrome1 = expand_from_center(i, i)
            palindrome2 = expand_from_center(i, i + 1)
            
            if len(palindrome1) > len(longest):
                longest = palindrome1
            if len(palindrome2) > len(longest):
                longest = palindrome2
        
        return longest