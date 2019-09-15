class Solution(object):
    def prefixesDivBy5(self, A):
        """
        :type A: List[int]
        :rtype: List[bool]
        """
        result = []
        sum = 0
        
        for i in A:
            sum = sum * 2 + i
            if sum % 5 == 0:
                result.append(True)
            else:
                result.append(False)
        return result