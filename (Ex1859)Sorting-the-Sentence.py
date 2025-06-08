class Solution(object):
    def sortSentence(self, s):
        """
        :type s: str
        :rtype: str
        """
        final = []
        words = s.split()
        sorted_words = sorted(words,key=lambda x:x[-1])
        for word in sorted_words:
            final.append(word[-2::-1][::-1])
        return " ".join(final)