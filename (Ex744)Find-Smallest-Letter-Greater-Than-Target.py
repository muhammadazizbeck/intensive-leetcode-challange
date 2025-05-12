class Solution(object):
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        # solution1
        # left, right = 0, len(letters) - 1
        # while left <= right:
        #     mid = (left + right) // 2
        #     if letters[mid] <= target:
        #         left = mid + 1
        #     else:
        #         right = mid - 1

        # return letters[left % len(letters)]

        # solution2
        def search(left,right):
            if left>right:
                return letters[left%len(letters)]
            mid = (left+right)//2
            if letters[mid] <= target:
                return search(mid+1,right)
            else:
                return search(left,mid-1)
        return search(0,len(letters)-1)