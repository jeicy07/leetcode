class Solution(object):
    def findCheapestPrice(self, n, flights, src, dst, K):
        """
        :type n: int
        :type flights: List[List[int]]
        :type src: int
        :type dst: int
        :type K: int
        :rtype: int
        """
        f = collections.defaultdict(dict)   #{dict {dict}}  not list
        for s, d, p in flights:
            f[s][d] = p
        
        heap = [(0, src, K+1)]  #build a min heap
        
        while heap:
            p, i, k = heapq.heappop(heap)
            if i == dst:
                return p
            if k > 0:
                for j in f[i]:
                    heapq.heappush(heap,(p + f[i][j], j, k-1))
                    
        return -1