class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # for i in range(len(nums)-1):
        #     for j in range(1,len(nums)):
        #         if nums[i]+nums[j]==target:
        #             return [i,j]

        dictionary = {}
        for i in range(len(nums)):
            num = nums[i]
            c = target - num
            if c in dictionary:
                return [dictionary[c], i]
            dictionary[num] = i
        return []
            
        