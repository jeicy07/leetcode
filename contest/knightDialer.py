class Solution(object):
    def knightDialer(self, N):
        import copy
        """
        :type N: int
        :rtype: int
        """
        twoHop = [[4,6], [6,8], [9,7], [1,8], [3,9,0], [-1], [1,7,0], [2,6], [1,3], [2,4]]  
        num = [2, 2, 2, 2, 3, 0, 3, 2, 2, 2] 
        current = copy.deepcopy(twoHop)

        
        cnt = 0
        if N is 1:
            return 10
        elif N is 2:
            return 20
        else:
            for i in range(3,N+1):
                for number in current:
                    tmp = []
                    for tail in number:
                        if tail != -1:
                            cnt += num[tail]
                            for numss in twoHop[tail]:
                                if numss != []:
                                    tmp.append(numss)
                        else:
                            tmp.append(-1)
                        
                    number = tmp
            return cnt
            


class Solution:
    def knightDialer(self, N):
        """
        :type N: int
        :rtype: int
        """ 
        dct = {1:[6, 8], 2:[7, 9], 3:[4, 8], 4:[0, 3, 9], 5:[], 6:[0, 1, 7], 7:[2, 6], 8:[1, 3], 9:[2, 4], 0:[4, 6]}
        
        dp = [1] * 10
        for _ in range(N - 1):
            nxt = [0] * 10
            for i in range(10):
                for j in dct[i]:
                    nxt[j] += dp[i]
            dp = nxt
        
        return sum(dp) % (10 ** 9 + 7)


        