class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        dictionary = Counter(s)
        for i in range(len(s)):
            if dictionary[s[i]]==1:
                return i
        return -1