class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # solution1
        # name=two pointer
        left,right = 0,len(height)-1
        max_water = 0
        while left<right:
            width = right-left
            height1 = min(height[left],height[right])
            max_water = max(max_water,width*height1)
            if height[left]<height[right]:
                left += 1
            else:
                right -= 1
        return max_water 