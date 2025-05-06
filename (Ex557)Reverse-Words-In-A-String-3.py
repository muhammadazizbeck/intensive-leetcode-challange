class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        rets = s.split()
        next_list = [ret[::-1] for ret in rets]
        return " ".join(next_list)
