class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        a=0
        for i in range(len(nums)):
            if target>nums[i]:
                a+=1
        return a
        