class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j]==target:
                    return [i,j]


        #Optimized solution

        # hash_map = {} ---------------- Hashmap used
        # for i, num in enumerate(nums):
        #     complement = target - num
        #     if complement in hash_map:
        #         return [hash_map[complement], i]
        #     hash_map[num] = i        
        # return []