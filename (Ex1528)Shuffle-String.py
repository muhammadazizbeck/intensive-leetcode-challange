class Solution(object):
    def restoreString(self, s, indices):
        """
        :type s: str
        :type indices: List[int]
        :rtype: str
        """
        return "".join([x for x, i in sorted(zip(s, indices), key=lambda x: x[1])])