class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        #Brute Force
        # for i in range(0,len(nums)-1):
        #     for j in range(i+1,len(nums)):
        #         if nums[i]+nums[j]==target:
        #             return [i,j]

        #Hashtable

        dict={}
        for i,num in enumerate(nums):
            difference=target-num
            if difference in dict:
                return [dict[difference],i]
            dict[num]=i
