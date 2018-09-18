class Solution(object):
    def checkPossibility(self, nums):
        numlen = len(nums)
        if numlen == 0 or numlen == 1 or numlen == 2:
            return True
        else:
            revised = False
            if nums[0] > nums[1]:
                revised = True
            for i in range(1, numlen - 1):
                if nums[i] > nums[i+1] and revised == True:
                    return False
                elif nums[i] > nums[i+1]:
                    if i == numlen - 2:
                        return True
                    elif nums[i] <= nums[i+2]:
                        revised = True
                    elif nums[i-1] <= nums[i+1]:
                        revised = True
                    else:
                        return False
                i = i + 1
                
            
            return True
                        
                    
        """
        :type nums: List[int]
        :rtype: bool
        """
        