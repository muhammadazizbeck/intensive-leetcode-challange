class Solution(object):
    def prefixCount(self, words, pref):
        """
        :type words: List[str]
        :type pref: str
        :rtype: int
        """
        ret = len(pref)
        counter = 0
        for word in words:
            if pref == word[:ret]:
                counter += 1
        return counter
        