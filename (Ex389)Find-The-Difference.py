class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        # solution1
        # count_s = Counter(s)
        # count_t = Counter(t)
        
        # for ch in count_t:
        #     if count_t[ch] != count_s.get(ch, 0):
        #         return ch

        # solution2
        return chr(sum(map(ord,t))-sum(map(ord,s)))

        # solution3
        # s = sorted(s)
        # t = sorted(t)

        # for i in range(len(s)):
        #     if s[i] != t[i]:
        #         return t[i]
        # return t[-1]