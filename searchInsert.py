class Solution(object):
    def searchInsert(self, nums, target):
        if nums is None:
            return 0
        i = 0
        numslen = len(nums)
        while (i < numslen and nums[i] < target):
            i = i + 1
        if i == numslen:
            return numslen
        else:
            return i
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """