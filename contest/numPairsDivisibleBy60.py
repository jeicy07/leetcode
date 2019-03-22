class Solution(object):
    def numPairsDivisibleBy60(self, time):
        """
        :type time: List[int]
        :rtype: int
        """
        num = 0
        
        res = {}
        for ele in time:
            left = ele % 60
            rest = (60 - left) % 60
            if res.has_key(rest):
                num += res[rest]
            if res.has_key(left):
                res[left] += 1
            else:
                res[left] = 1
                
        return num
        