class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # solution1
        # name=two pointers
        nums.sort()
        closest = float("inf")
        for i in range(len(nums)-1):
            left,right=i+1,len(nums)-1
            while left<right:
                current = nums[i]+nums[left]+nums[right]
                if abs(target-current)<abs(target-closest):
                    closest = current
                if current<target:
                    left += 1
                elif current>target:
                    right -= 1
                else:
                    return target
        return closest

