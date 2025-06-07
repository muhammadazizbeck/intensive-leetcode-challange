class Solution(object):
    def findWordsContaining(self, words, x):
        """
        :type words: List[str]
        :type x: str
        :rtype: List[int]
        """
        # solution1
        # txt = []
        # for index,value in enumerate(words):
        #     if x in value:
        #         txt.append(index)
        # return txt

        # solution2
        return [i for i,w in enumerate(words) if x in w]

        # solution3
        # txt = []
        # for i in range(len(words)):
        #     if x in words[i]:
        #         txt.append(i)
        # return txt