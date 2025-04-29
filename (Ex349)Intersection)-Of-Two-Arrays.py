class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        # solution1
        # name=set
        set1 = set(nums1)
        set2 = set(nums2)
        res = []
        for i in set1:
            if i in set2:
                res.append(i)
        return res

        # solution2
        # final = [num1 for num1 in nums1 if num1 in nums2]
        # return list(set(final))