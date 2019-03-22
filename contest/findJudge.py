class Solution(object):
    def findJudge(self, N, trust):
        """
        :type N: int
        :type trust: List[List[int]]
        :rtype: int
        """
        if N == 1:
            return 1
        elif len(trust) < N-1:
            return -1
        else:
            trust.sort(key = lambda x:(x[1], x[0]))
            c = [x[0] for x in trust]
            cnt = 0

            if trust[0][1] not in c:
                judge = trust[0][1]
            else:
                judge = -1
                
            for unit in trust:
                if unit[1] != judge:
                    if cnt == N-1:
                        return judge
                    else:                      
                        if unit[1] not in c:
                            judge = unit[1]
                            cnt = 1
                else:
                    cnt = cnt + 1
            
            if cnt == N-1:
                return judge