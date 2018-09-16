class Solution(object):
    def sortArrayByParity(self, A):
        if A is None:
            return A
        else:
            even = list()
            odd = list()
            for a in A:
                if a%2 == 0:
                    even.append(a)
                else:
                    odd.append(a)
            even = even + odd
        return even
        """
        :type A: List[int]
        :rtype: List[int]
        """