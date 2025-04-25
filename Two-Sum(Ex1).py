class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # solution1
        # name:Brute Force
        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)):
        #         if nums[i]+nums[j]==target:
        #             return [i,j]

        # solution2
        name:hashmap(dictionary)
        hashmap = {}
        for index,value in enumerate(nums):
            intarget = target-value
            if intarget in hashmap:
                return [hashmap[intarget],index]
            hashmap[value] = index

        # solution3
        # name:two pointers
        # sorted_nums = sorted((num,i)for i,num in enumerate(nums))
        # left,right = 0,len(nums)-1

        # while left < right:
        #     total = sorted_nums[left][0]+sorted_nums[right][0]
        #     if total == target:
        #         return [sorted_nums[left][1],sorted_nums[right][1]]
        #     elif total < target:
        #         left += 1
        #     else:
        #         right -= 1

        # solution4
        # name:Set searching
        # seen = set()
        # for num in nums:
        #     intarget = target-num
        #     if intarget in seen:
        #         return [nums.index(intarget),nums.index(num) if num != intarget else nums.index(num,nums.index(intarget)+1)]
        #     seen.add(num)

        #solution5
        # name:binary search
        # sorted_nums = sorted((num, i) for i, num in enumerate(nums))
    
        # for i in range(len(sorted_nums)):
        #     intarget = target - sorted_nums[i][0]
        #     left, right = i + 1, len(sorted_nums) - 1
            
        #     while left <= right:
        #         mid = (left + right) // 2  
        #         if sorted_nums[mid][0] == intarget:
        #             return [sorted_nums[i][1], sorted_nums[mid][1]]
        #         elif sorted_nums[mid][0] < intarget:
        #             left = mid + 1 
        #         else:
        #             right = mid - 1  
        
        # return []

        # solution6
        # name:recursion
        # def recursion(index):
        #     if index == len(nums):
        #         return None
        #     for i in range(index+1,len(nums)):
        #         if nums[index]+nums[i]==target:
        #             return [index,i]
        #     return recursion(index+1)
        # return recursion(0)