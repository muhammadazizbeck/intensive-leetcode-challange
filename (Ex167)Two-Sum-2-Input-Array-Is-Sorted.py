class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        # solution1
        left,right = 0,len(numbers)-1
        while left<right:
            value = numbers[left]+numbers[right]
            if value==target:
                return [left+1,right+1]
            elif value>target:
                right -= 1
            else:
                left += 1
        
        # solution2
        # num_map = {} 
        # for i, num in enumerate(numbers):
        #     complement = target - num
        #     if complement in num_map:
        #         return [num_map[complement] + 1, i + 1]
        #     num_map[num] = i
            
            