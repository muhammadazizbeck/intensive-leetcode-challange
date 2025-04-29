class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # solution1
        # name = list comprehension
        # cleaned = [ch.lower() for ch in s if ch.isalnum()]  # harf yoki raqam
        # return cleaned == cleaned[::-1]
        
        # solution2
        # name=two pointers
        # left,right = 0,len(s)-1
        # while left<right:
        #     while left<right and not s[left].isalnum():
        #         left += 1
        #     while left<right and not s[right].isalnum():
        #         right -= 1
        #     if s[left].lower() != s[right].lower():
        #         return False
        #     left += 1
        #     right -= 1
        # return True

        # solution3
        # stack = []
        # for c in s:
        #     if c.isalnum():
        #         stack.append(c.lower())
        # return stack==stack[::-1]

        # solution4
        final = "".join(filter(lambda c: c.isalnum(),s)).lower()
        return final==final[::-1]