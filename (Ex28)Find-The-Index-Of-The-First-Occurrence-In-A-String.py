class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        # solution1
        # name=sliding window
        k = len(needle)
        if k==0:
            return 0
        for i in range(len(haystack)-k+1):
            if haystack[i:i+k]==needle:
                return i
            else:
                continue
        return -1

        # solution2
        # k = len(needle)
        # res = []
        # for i in range(len(haystack)-k+1):
        #     res.append(haystack[i:i+k])

        # for substr in res:
        #     if substr == needle:
        #         return res.index(substr)
        #         break
        # return -1