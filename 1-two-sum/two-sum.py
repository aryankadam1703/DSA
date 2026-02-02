class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # Inefficient
        # for i in range(len(nums)-1):                                  # Time complexity O(n^2)
        #     for j in range(i+1,len(nums)):                            # Space Complexity O(1)
        #         if nums[i]+nums[j] == target:
        #             return [i,j]

        num_map = {}
        for i,num in enumerate(nums):              # Enumerate return pairs of (index,value)
            complement = target-num
            if complement in num_map:
                return [num_map[complement],i]      # Here i is index of num(which is iterating in the nums list)
            num_map[num] = i