class Solution(object):
    def sortPeople(self, names, heights):
        """
        :type names: List[str]
        :type heights: List[int]
        :rtype: List[str]
        """
        return [name for name,height in sorted(zip(names,heights),key=lambda x:x[1],reverse=True)]