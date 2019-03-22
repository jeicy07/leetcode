class Solution(object):
    def largestSumAfterKNegations(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """

        neg = []
        pos = []
        for i in A:
            if i < 0:
                neg.append(i)
            else:
                pos.append(i)
                
        neg.sort()
        negCnt = len(neg)
        posCnt = len(pos)
        
        if K >= negCnt:
            negNew = [-x for x in neg]
            if (K-negCnt) % 2 == 0:
                return sum(negNew) + sum(pos)
            else:
                pos.extend(negNew)
                print pos
                print sum(pos)
                print min(pos)
                result = sum(pos) - 2 * min(pos)
                return result
        else:
            i = 0
            while K-i > 0:
                neg[i] = -neg[i]
                i = i + 1              
            return sum(neg) + sum(pos)